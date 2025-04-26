from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.program import ProgramCreate, ProgramOut
from app.models.program import HealthProgram
from app.database.session import SessionLocal

router = APIRouter(prefix="/programs", tags=["Programs"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ProgramOut)
def create_program(program: ProgramCreate, db: Session = Depends(get_db)):
    db_program = db.query(HealthProgram).filter(HealthProgram.name == program.name).first()
    if db_program:
        raise HTTPException(status_code=400, detail="Program already exists")
    
    new_program = HealthProgram(**program.dict())
    db.add(new_program)
    db.commit()
    db.refresh(new_program)
    return new_program
