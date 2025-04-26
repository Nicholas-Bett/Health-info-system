from pydantic import BaseModel

class ProgramBase(BaseModel):
    name: str
    description: str

class ProgramCreate(ProgramBase):
    pass

class ProgramOut(ProgramBase):
    id: int

    class Config:
        orm_mode = True
