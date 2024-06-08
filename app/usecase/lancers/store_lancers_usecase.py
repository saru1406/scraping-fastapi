from sqlalchemy.orm import Session
from fastapi import Depends
from app.repositories.lancers.lancers_repository import LancersRepository

class StoreLnacersUsecase:
    def __init__(self, lancers_repository: LancersRepository = Depends(LancersRepository)) -> None:
        self.lancers_repository = lancers_repository
    
    async def execute(self, db: Session):
        await self.lancers_repository.fetch_lancers()
        
