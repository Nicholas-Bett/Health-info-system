from fastapi import FastAPI

# Initialize the FastAPI application with a title
app = FastAPI(title="Health Info System")

# Include the program, client, and enrollment routers
from app.routes import program, client, enrollment

app = FastAPI(title="Health Info System")

app.include_router(program.router)
app.include_router(client.router)
app.include_router(enrollment.router)

# Define a route for the root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to the Health Information System"}
