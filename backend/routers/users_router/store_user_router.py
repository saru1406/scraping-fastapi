from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.repositories.user.user_repository import UserRepository
from backend.schemas.user_schema import UserSchema, UserSchemaCreate

router = APIRouter()


@router.post("/users/", response_model=UserSchema, tags=["ユーザー"])
def create_user(
    user: UserSchemaCreate,
    db: Session = Depends(get_db),
    userRepository: UserRepository = Depends(UserRepository),
):
    db_user = userRepository.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return userRepository.create_user(db=db, user=user)
