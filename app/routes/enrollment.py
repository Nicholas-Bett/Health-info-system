from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.session import SessionLocal
from app.models.enrollment import Enrollment
from app.models.client import Client
from app.models.program import HealthProgram

# Initialize the router with a prefix and tags
router = APIRouter(prefix="/enrollments", tags=["Enrollments"])

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint to enroll a client in a health program
@router.post("/")
def enroll_client(client_id: int, program_id: int, db: Session = Depends(get_db)):
    # Fetch the client by ID
    client = db.query(Client).filter(Client.id == client_id).first() 
    # Fetch the health program by ID
    program = db.query(HealthProgram).filter(HealthProgram.id == program_id).first()
    
    # Check if both client and program exist
    if not client or not program:
        raise HTTPException(status_code=404, detail="Client or Program not found")

    # Create a new enrollment record
    enrollment = Enrollment(client_id=client_id, program_id=program_id)
    db.add(enrollment)
    db.commit()
    # Return a success message
    return {"message": "Client enrolled in program"}
