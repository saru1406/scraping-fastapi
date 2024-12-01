from typing import List

from sqlalchemy.orm import Session

from backend.models.job import Job


class JobRepository:
    async def store(self, db: Session, job_objects: list) -> None:
        db.bulk_save_objects(job_objects)

    def fetchSelect(self, db: Session) -> List[Job]:
        return db.query(Job).limit(1000).all()
    
    def fetch(self, db: Session) -> List[Job]:
        return db.query(Job).all()

    async def delete(self, db: Session) -> None:
        db.query(Job).delete()
