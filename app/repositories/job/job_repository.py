from sqlalchemy.orm import Session
from typing import List

from app.models.job import Job

class JobRepository:
    async def store(self, db: Session, job_objects: list) -> None:
        db.bulk_save_objects(job_objects)
        
    async def fetch(self, db:Session, limit: int = 100) -> List[Job]:
        return db.query(Job).limit(limit).all()
