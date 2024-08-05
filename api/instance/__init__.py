from fastapi import APIRouter
from utils import data_info, mcsm
import config

instance = APIRouter(
    prefix="/instance",
    tags=["instance"]
)

mcsm_instance = mcsm.Mcsm(url=config.get("panel","url"), apikey=config.get("panel","apikey"))

@instance.get("/gameinfo")
def gameinfo(id=None):
    """
    获取游戏信息
    """
    if id == None:
        data = data_info.get("gameinfo/games.json")
    else:
        data = data_info.get("gameinfo/" + id + ".json")
    return data

@instance.post("/create")
def create(data: type.create):
    uuid = mcsm_instance.add_example(data.name, data.type)
    return_msg = {
        "code": 200,
        "msg": "success",
        "data": {
            "uuid": uuid
        }
    }
    return return_msg