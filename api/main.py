from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import config
from user import user
from info import info
from point import point
from instance import instance

app = FastAPI()
app.include_router(user)
app.include_router(info)
app.include_router(point)
app.include_router(instance)

@app.get("/")
def home():
    url = config.get("links","main")
    return RedirectResponse(url)