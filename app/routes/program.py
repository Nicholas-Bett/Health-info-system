from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.program import ProgramCreate, ProgramOut
from app.models.program import HealthProgram
from app.database.session import SessionLocal

# Initialize the router with a prefix and tags
router = APIRouter(prefix="/programs", tags=["Programs"])

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint to create a new health program
@router.post("/", response_model=ProgramOut)
def create_program(program: ProgramCreate, db: Session = Depends(get_db)):
    # Check if the program already exists in the database
    db_program = db.query(HealthProgram).filter(HealthProgram.name == program.name).first()
    if db_program:
        raise HTTPException(status_code=400, detail="Program already exists")
    
    # Create a new program instance and add it to the session
    new_program = HealthProgram(**program.dict())
    db.add(new_program)
    db.commit()
    db.refresh(new_program)
    # Return the newly created program
    return new_program
