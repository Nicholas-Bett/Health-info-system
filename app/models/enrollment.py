from sqlalchemy import Column, Integer, ForeignKey, Table
from app.database.base import Base

# SQLAlchemy model for the 'Enrollment' table
class Enrollment(Base):
    __tablename__ = "enrollments" # Define the table name in the database

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    program_id = Column(Integer, ForeignKey("health_programs.id"))
