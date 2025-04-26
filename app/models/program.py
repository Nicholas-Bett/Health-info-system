from sqlalchemy import Column, Integer, String
from app.database.base import Base

class HealthProgram(Base):
    __tablename__ = "health_programs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
