from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Retrieve the database URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

# Create the SQLAlchemy engine to manage DB connections
engine = create_engine(DATABASE_URL)

# Create a session factory to interact with the database
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
