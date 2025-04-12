from pydantic import BaseModel

class login(BaseModel):
    username: str
    password: str

class register(BaseModel):
    email: str
    avatar: str
    username: str
    password: str

class active(BaseModel):
    email: str
    active_code: int
    username: str
    panel_password: str