from fastapi import APIRouter
from user import type,verify_content

user = APIRouter(
    prefix="/user",
    tags=["user"]
)

@user.post("/register")
def register(data: type.register):
    # 邮箱判断
    if verify_content.email(data.email) == False :
        return_content = {
            "code": 500,
            "message": "邮箱格式错误"
        }
        return return_content
    
    return data

@user.post("/login")
def login(data: type.login):
    # 验证逻辑 没写完
    return_content = {
        "code": 500,
        "message": "用户名或密码错误"
    }
    return return_content