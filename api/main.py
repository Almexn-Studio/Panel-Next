from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from config import get_config
from user import user

app = FastAPI()
app.include_router(user)

@app.get("/")
def home():
    url = get_config("links","main")
    return RedirectResponse(url)