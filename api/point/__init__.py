import random
import time
from typing import Optional
from fastapi import APIRouter, Cookie
from utils import database, token

point = APIRouter(
    prefix="/point",
    tags=["point"]
)

@point.get("/sign")
def sign(fucubemc_jwt: Optional[str] = Cookie(None)):
    status, info, msg = token.verify(fucubemc_jwt)
    points = random.randint(10, 50)
    sign_info = {
        "username": info["username"],
        "points": points,
        "time": info["sign_time"]
    }
    database.update_document("user",{
        "username":info["username"]
        },{
            "$set":{
                "points": info["pints"]+points,
                "point_last": int(time.time())
                }
        })
    database.add_document("sign_log",sign_info)
    return_msg = {
        "code": 200,
        "point": points,
        "msg": msg
    }
    return return_msg