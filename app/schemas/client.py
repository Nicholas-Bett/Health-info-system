from pydantic import BaseModel
from typing import List, Optional

class ClientBase(BaseModel):
    full_name: str
    age: int
    gender: str
    contact: str

class ClientCreate(ClientBase):
    pass

class ClientOut(ClientBase):
    id: int

    class Config:
        orm_mode = True
