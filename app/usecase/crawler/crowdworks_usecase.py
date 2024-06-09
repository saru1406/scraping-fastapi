from sqlalchemy.orm import Session
from fastapi import Depends

from app.repositories.crowdworks.crowdworks_repository import CrowdWorksRepository

class StoreCrowdWorksUsecase:
    def __init__(self, crowdworks_repository: CrowdWorksRepository = Depends(CrowdWorksRepository)):
        self.crowdworks_repository = crowdworks_repository
        
    def execute(self, db: Session):
        crowdworks = self.crowdworks_repository.fetch_crowdworks()
        print(crowdworks)
        