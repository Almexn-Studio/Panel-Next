from fastapi import APIRouter
from user import type

user = APIRouter(
    prefix="/user",
    tags=["user"]
)

@user.post("/login")
def login(data: type.login):
    return data