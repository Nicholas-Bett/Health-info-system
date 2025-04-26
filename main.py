from fastapi import FastAPI
from app.routes import program, client, enrollment

app = FastAPI(title="Health Info System")

app.include_router(program.router)
app.include_router(client.router)
app.include_router(enrollment.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Health Information System"}
