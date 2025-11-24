from datetime import timedelta
from typing import Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.services.user_service import get_user_by_username
from app.core.security import verify_password, create_access_token
from app.core.config import settings

def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    if not user.is_active:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User is inactive")
    return user

def create_user_token(user, expires_minutes: Optional[int] = None):
    delta = timedelta(minutes=expires_minutes) if expires_minutes else timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(subject=user.username, expires_delta=delta)
    return token
