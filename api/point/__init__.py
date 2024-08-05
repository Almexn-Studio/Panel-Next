from fastapi import APIRouter

user = APIRouter(
    prefix="/point",
    tags=["point"]
)