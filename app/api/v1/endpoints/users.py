from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session

from app.schemas.user import UserOut
from app.api.deps import get_db, get_current_active_user
from app.services.user_service import list_users

router = APIRouter()

@router.get("/me", response_model=UserOut)
def read_current_user(current_user = Depends(get_current_active_user)):
    return current_user

@router.get("/", response_model=List[UserOut])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = list_users(db, skip=skip, limit=limit)
    return users
