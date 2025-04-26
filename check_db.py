# check_db.py
from app.database import SessionLocal
from app.models import Client, HealthProgram, Enrollment

db = SessionLocal()

print("\n--- Clients ---")
for client in db.query(Client).all():
    print(client.id, client.full_name, client.email)

print("\n--- Programs ---")
for program in db.query(Program).all():
    print(program.id, program.name, program.description)

print("\n--- Enrollments ---")
for enroll in db.query(Enrollment).all():
    print(enroll.client_id, enroll.program_id)

db.close()
