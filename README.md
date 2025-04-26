# Health Information System – CEMA Internship Assessment

A simple health information API system for managing clients and health programs.

## Features
- Create health programs (HIV, TB, etc.)
- Register new clients
- Enroll clients in multiple programs
- View/search client profiles
- API-first approach with FastAPI
- RESTful endpoints with Swagger UI

## Tech Stack
- Python
- FastAPI
- PostgreSQL
- SQLAlchemy + Alembic
- Pytest (for testing)

## Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/Nicholas-Bett/Health-info-system.git
   cd Health-info-system

2. Set up your environment:
    ```bash
    python -m venv venv
    source venv/Scripts/activate  # Windows
    pip install -r requirements.txt

3. Configure your .env:
    ```bash
    DATABASE_URL=postgresql+psycopg2://postgres:yourpassword@localhost/health_info_db

4. Run migrations:
    ```bash
    alembic upgrade head

5. Start the server:
    ```bash
    uvicorn main:app --reload

6. Visit docs at: http://localhost:8000/docs