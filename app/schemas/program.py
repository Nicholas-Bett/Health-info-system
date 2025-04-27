from pydantic import BaseModel, ConfigDict

class ProgramBase(BaseModel):
    name: str
    description: str

class ProgramCreate(ProgramBase):
    pass

class ProgramOut(ProgramBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
