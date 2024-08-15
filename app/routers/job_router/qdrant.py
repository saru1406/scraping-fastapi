from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.usecase.qdrant.qdrant_usecase import QdrantUsecase

router = APIRouter()


@router.post("/qdrant", tags=["qdrant保存"])
def test(
    db: Session = Depends(get_db),
    qdrant_usecase: QdrantUsecase = Depends(QdrantUsecase),
):
    qdrant_usecase.store_qdrant_by_job(db=db)
