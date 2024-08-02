from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import config
from user import user

app = FastAPI()
app.include_router(user)

@app.get("/")
def home():
    url = config.get("links","main")
    return RedirectResponse(url)