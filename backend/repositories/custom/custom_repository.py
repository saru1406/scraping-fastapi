from sqlalchemy.orm import Session
from backend.models.custom import Custom

class CustomRepository:
    def store(self, db: Session, custom: Custom):
        db.add(custom)
