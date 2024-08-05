from fastapi import APIRouter
from utils import data_info

info = APIRouter(
    prefix="/info",
    tags=["info"]
)

error_code = 403
return_content = {
    "code": 200,
    "message": "success"
}

@info.get("/notices")
def notices():
    info = data_info.get("info/notices.json")
    return info

@info.get("/ads")
def ads():
    info = data_info.get("info/ads.json")
    return info