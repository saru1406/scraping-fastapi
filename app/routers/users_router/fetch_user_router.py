from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.repositories.user.user_repository import UserRepository
from app.schemas.user_schema import UserSchema

router = APIRouter()


@router.get("/users/", response_model=list[UserSchema], tags=["ユーザー"])
def read_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    userRepository: UserRepository = Depends(UserRepository),
):
    users = userRepository.get_users(db, skip=skip, limit=limit)
    return users
