from fastapi import FastAPI
from app.api.v1.endpoints import users

app = FastAPI(title="FastAPI Robust App")

app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])

@app.get("/")
def root():
    return {"message": "FastAPI is running"}
