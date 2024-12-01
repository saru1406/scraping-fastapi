from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.usecase.custom.store_custom_usecase import StoreCustomUsecase

router = APIRouter()


@router.post("/custom", tags=["customデータ保存"])
def store_custom(
    db: Session = Depends(get_db),
    store_custom_usecase: StoreCustomUsecase = Depends(StoreCustomUsecase),
):
    store_custom_usecase.execute(db=db)
