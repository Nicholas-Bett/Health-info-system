from pydantic import BaseModel, ConfigDict
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

    model_config = ConfigDict(from_attributes=True)
