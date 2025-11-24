from fastapi import FastAPI
from app.api.v1.endpoints import users, auth

app = FastAPI(title="FastAPI Robust App")

app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])


@app.get("/")
def root():
    return {"message": "FastAPI is running"}

@app.get("/health")
def health():
    return {"status": "ok"}