from fastapi import APIRouter
from utils import database

point = APIRouter(
    prefix="/point",
    tags=["point"]
)

@point.get("/sign")
def sign():
    database.add_document("sign_log",)
    return "Hello World"