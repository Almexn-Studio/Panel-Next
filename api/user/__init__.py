import random
from typing import Optional
from fastapi import APIRouter, Cookie
from user import type,verify_content
from utils import database, token, email, mcsm
import hashlib
import config

user = APIRouter(
    prefix="/user",
    tags=["user"]
)

error_code = 403
return_content = {
    "code": 200,
    "message": "success"
}

mcsm_instance = mcsm.Mcsm(url=config.get("panel","url"), apikey=config.get("panel","apikey"))

@user.get("/")
def get_user(fucubemc_jwt: Optional[str] = Cookie(None)):
    status, info, msg = token.verify(fucubemc_jwt)
    if status == False:
        return_content = {
            "code": error_code,
            "message": msg
        }
        return return_content
    else:
        return_content = {
            "code": 200,
            "message": "success",
            "data": {
                "username": info["username"],
                "avatar": info["avatar"],
                "email": info["email"],
                "role": info["role"],
                "points": info["points"],
                "point_last": info["point_last"]
            }
        }

@user.post("/active")
def active(data: type.active):
    # 邮箱判断
    if verify_content.email(data.email) == False :
        return_content = {
            "code": error_code,
            "message": "邮箱格式错误"
        }
        return return_content
    user_info = database.get_document("users",{"username":data.username})
    if user_info == []:
        return_content = {
            "code": error_code,
            "message": "用户不存在"
        }
        return return_content
    if user_info[0]["email"] == data.email and user_info[0]["role"] == "guest":
        if user_info[0]["active_code"] == data.active_code:
            success, uuid_or_error = mcsm_instance.create_user(username=data.username, password=data.panel_password)
            if success:
                database.update_document("users",{"username":data.username},{"$set":{"role":"user"}})
                return_content = {
                    "code": 200,
                    "message": "success"
                }
                return return_content
            else:
                return_content = {
                    "code": error_code,
                    "message": uuid_or_error
                }
        else:
            return_content = {
                "code": error_code,
                "message": "激活码错误"
            }
    else:
        return_content = {
            "code": error_code,
            "message": "用户已注册"
        }
        return return_content

@user.post("/register")
def register(data: type.register):
    # 邮箱判断
    if verify_content.email(data.email) == False :
        return_content = {
            "code": error_code,
            "message": "邮箱格式错误"
        }
        return return_content
    # 重名判断
    if database.get_document("users",{"username":data.username}) != []:
        return_content = {
            "code": error_code,
            "message": "用户名已存在"
        }
        return return_content
    # 数据库操作
    hash_password = hashlib.sha256(data.password.encode("utf-8"))
    doc = [
        {
            "username": data.username,
            "avatar": data.avatar,
            "email": data.email,
            "password": hash_password.hexdigest(),
            "role": "guest",
            "points": 10,
            "point_last": 0,
            "active_code": str(random.randint(100000,999999))# 激活码
        }
    ]
    replace= {
        "links[main]": str(config.get("links","main")),
        "email[1]": data.email,
        "usn[1]": data.username,
        "act_cd[1]": doc[0]["active_code"]
    }
    # email.send_template(data.email, "FuCubeMC - 激活账号", "active", replace)
    db_return = database.add_document("users",doc)
    ids = db_return.inserted_ids
    if ids == []:
        return_content = {
            "code": error_code,
            "message": "注册失败，错误信息："+db_return
        }
        return return_content
    return return_content

@user.post("/login")
def login(data: type.login):
    # 存在检查
    verify_user = {
        "username":data.username,
        "password":hashlib.sha256(data.password.encode("utf-8")).hexdigest()
    }
    result = database.get_document("users",verify_user)
    if result == []:
        return_content = {
            "code": error_code,
            "message": "用户名或密码错误"
        }
        return return_content
    else:
        for for_data in result:
            if for_data["role"] == "guest":
                return_content = {
                    "code": error_code,
                    "message": "用户未激活"
                }
                return return_content
    return_content = {
        "code": 200,
        "message": "success",
        "data": {
            "token": token.create(result)
        }
    }
    return return_content