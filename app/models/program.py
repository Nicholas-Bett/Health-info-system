from sqlalchemy import Column, Integer, String
from app.database.base import Base

# SQLAlchemy model for the 'HealthProgram' table
class HealthProgram(Base):
    __tablename__ = "health_programs"  # Define the table name in the database

    # Define the columns for the "health_programs" table
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
