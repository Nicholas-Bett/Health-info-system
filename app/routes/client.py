from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.client import ClientCreate, ClientOut
from app.models.client import Client
from app.database.session import SessionLocal

router = APIRouter(prefix="/clients", tags=["Clients"])

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new client
@router.post("/", response_model=ClientOut)
def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    new_client = Client(**client.dict())
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client

# Get all clients
@router.get("/", response_model=list[ClientOut])
def get_clients(db: Session = Depends(get_db)):
    return db.query(Client).all()

# Get a client by ID
@router.get("/{client_id}", response_model=ClientOut)
def get_client_by_id(client_id: int, db: Session = Depends(get_db)):
    client = db.query(Client).filter(Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client
