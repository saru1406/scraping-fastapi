from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.usecase.job.fetch_job_usecase import FetchJobUsecase

router = APIRouter()


@router.get("/jobs", tags=["案件取得"])
async def fetch_job(
    job_usecase: FetchJobUsecase = Depends(FetchJobUsecase),
    db: Session = Depends(get_db),
):
    return await job_usecase.fetch(db=db)
