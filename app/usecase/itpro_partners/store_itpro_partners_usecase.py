from sqlalchemy.orm import Session
from fastapi import Depends
from app.repositories.itpro_partners.itpro_partners_repository import ItproPartnersRepository

class ItproPartnersUsecase:
    def __init__(self, itpro_partners: ItproPartnersRepository = Depends(ItproPartnersRepository)) -> None:
        self.itpro_partners = itpro_partners
    
    async def execute(self, db: Session):
        await self.itpro_partners.fetch_itpro_partners()
    