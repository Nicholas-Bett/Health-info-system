from sqlalchemy import Column, Integer, ForeignKey, Table
from app.database.base import Base

class Enrollment(Base):
    __tablename__ = "enrollments"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    program_id = Column(Integer, ForeignKey("health_programs.id"))
