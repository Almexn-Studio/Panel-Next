from fastapi import APIRouter

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
def register():
    info = {
        "id": 1,
        "title": "FuCubeMC创建啦！",
        "content": "喜大普奔，FuCubeMC创建啦！",
        "type": "我是公告类型",
        "time": 0
    }
    return info

@info.get("/ads")
def ads():
    info = {
        "id": 1,
        "name": "FuCubeMC",
        "img":"我是广告图片"
    }
    return info