from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session

from backend.models.job import Job
from backend.repositories.job.job_repository import JobRepository


class FetchJobUsecase:
    def __init__(self, job_repository: JobRepository = Depends(JobRepository)) -> None:
        self.job_repository = job_repository

    def fetch(self, db: Session) -> List[Job]:
        return self.job_repository.fetchSelect(db=db)
