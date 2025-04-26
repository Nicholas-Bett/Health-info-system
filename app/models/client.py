from sqlalchemy import Column, Integer, String
from app.database.base import Base

# SQLAlchemy model for the 'clients' table
class Client(Base):
    __tablename__ = "clients" # Table name in the database

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    age = Column(Integer)
    gender = Column(String)
    contact = Column(String)
