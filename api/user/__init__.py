from fastapi import APIRouter
from user import type,verify_content
from utils import database
import hashlib

user = APIRouter(
    prefix="/user",
    tags=["user"]
)

@user.post("/register")
def register(data: type.register):
    return_content = {
        "code": 200,
        "message": "success"
    }
    # 邮箱判断
    if verify_content.email(data.email) == False :
        return_content = {
            "code": 500,
            "message": "邮箱格式错误"
        }
        return return_content
    # 重名判断
    if database.get_document("users",{"username":data.username}) != {}:
        return_content = {
            "code": 500,
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
            "password": hash_password.hexdigest()
        }
    ]
    db_return = database.add_document("users",doc)
    ids = db_return.inserted_ids
    if ids == []:
        return_content = {
            "code": 500,
            "message": "注册失败，错误信息："+db_return
        }
        return return_content
    return return_content

@user.post("/login")
def login(data: type.login):
    # 验证逻辑 没写完
    return_content = {
        "code": 500,
        "message": "用户名或密码错误"
    }
    return return_content