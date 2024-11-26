from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.repositories.user.user_repository import UserRepository
from backend.schemas.user_schema import UserSchema

router = APIRouter()


@router.get("/users/{user_id}", response_model=UserSchema, tags=["ユーザー"])
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = UserRepository.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
