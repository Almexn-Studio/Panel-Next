from fastapi import APIRouter
from user import type,verify_content
from utils import database, token
import hashlib

user = APIRouter(
    prefix="/user",
    tags=["user"]
)

error_code = 403
return_content = {
    "code": 200,
    "message": "success"
}

@user.get("/")
def get_user(token_data: str):
    status, info, msg = token.verify(token_data)
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
    hash_password = hashlib.md5(data.password.encode("utf-8"))
    doc = [
        {
            "username": data.username,
            "avatar": data.avatar,
            "email": data.email,
            "password": hash_password.hexdigest(),
            "role": "guest",
            "points": 10,
            "point_last": 0
        }
    ]
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
        "password":hashlib.md5(data.password.encode("utf-8")).hexdigest()
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