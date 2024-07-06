from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session

from app.models.job import Job
from app.repositories.job.job_repository import JobRepository


class FetchJobUsecase:
    def __init__(self, job_repository: JobRepository = Depends(JobRepository)) -> None:
        self.job_repository = job_repository

    async def fetch(self, db: Session) -> List[Job]:
        return await self.job_repository.fetch(db=db)
