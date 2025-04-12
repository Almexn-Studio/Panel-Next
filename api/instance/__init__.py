from typing import Optional
from fastapi import APIRouter, Cookie
from utils import token, data_info, mcsm
import config
from instance import type

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
def create(data: type.create, fucubemc_jwt: Optional[str] = Cookie(None)):
    instance_uuid = mcsm_instance.add_example(data.name, data.type)
    user_data = token.verify(fucubemc_jwt)
    user_uuid = mcsm_instance.get_uuid_by_name(user_data["username"])
    mcsm_instance.give_example(instance_uuid, user_uuid)
    return_msg = {
        "code": 200,
        "msg": "success",
        "data": {
            "user_uuid": user_uuid,
            "instance_uuid": instance_uuid
        }
    }
    return return_msg