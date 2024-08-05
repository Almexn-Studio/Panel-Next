from pydantic import BaseModel

class create(BaseModel):
    name: str
    type: str