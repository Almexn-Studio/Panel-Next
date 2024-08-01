from pydantic import BaseModel

class login(BaseModel):
    username: str
    password: str