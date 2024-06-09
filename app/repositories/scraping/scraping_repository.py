from sqlalchemy.orm import Session

class ScrapingRepository:
    
    async def store(self, db: Session, job_objects: list):
        db.bulk_save_objects(job_objects)
