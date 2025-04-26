from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.session import SessionLocal
from app.models.enrollment import Enrollment
from app.models.client import Client
from app.models.program import HealthProgram

router = APIRouter(prefix="/enrollments", tags=["Enrollments"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def enroll_client(client_id: int, program_id: int, db: Session = Depends(get_db)):
    client = db.query(Client).filter(Client.id == client_id).first()
    program = db.query(HealthProgram).filter(HealthProgram.id == program_id).first()
    
    if not client or not program:
        raise HTTPException(status_code=404, detail="Client or Program not found")

    enrollment = Enrollment(client_id=client_id, program_id=program_id)
    db.add(enrollment)
    db.commit()
    return {"message": "Client enrolled in program"}
