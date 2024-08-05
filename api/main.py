from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import config
from user import user
from info import info
from point import point

app = FastAPI()
app.include_router(user)
app.include_router(info)

@app.get("/")
def home():
    url = config.get("links","main")
    return RedirectResponse(url)