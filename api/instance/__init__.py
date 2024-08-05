from fastapi import APIRouter

instance = APIRouter(
    prefix="/instance",
    tags=["instance"]
)

@instance.get("/gameinfo")
def gameinfo():
    return "Hello World"