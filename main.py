from fastapi import FastAPI

app = FastAPI(title="Health Info System")

@app.get("/")
def root():
    return {"message": "Welcome to the Health Information System!"}
