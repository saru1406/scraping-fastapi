from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db

from app.usecase.job.fetch_job_usecase import FetchJobUsecase

router = APIRouter()

@router.get("/jobs", tags=['案件取得'])
async def fetch_job(
    job_usecase: FetchJobUsecase = Depends(FetchJobUsecase),
    db: Session = Depends(get_db)
):
    jobs = await job_usecase.fetch(db=db)
    return jobs
