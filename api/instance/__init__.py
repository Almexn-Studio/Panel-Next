from fastapi import APIRouter
from utils import data_info

instance = APIRouter(
    prefix="/instance",
    tags=["instance"]
)

@instance.get("/gameinfo")
def gameinfo(id=None):
    if id == None:
        data = data_info.get("gameinfo/games.json")
    else:
        data = data_info.get("gameinfo/" + id + ".json")
    return data