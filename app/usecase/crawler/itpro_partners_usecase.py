from sqlalchemy.orm import Session
from fastapi import Depends

from app.repositories.itpro_partners.itpro_partners_repository import ItproPartnersRepository
from app.repositories.job.job_repository import JobRepository
from app.usecase.crawler.crawler_base_usecase import CrawlerBaseUsecase

class StoreItproPartnersUsecase(CrawlerBaseUsecase):
    def __init__(
        self,
        itpro_partners_repository: ItproPartnersRepository = Depends(ItproPartnersRepository),
        job_repository: JobRepository = Depends(JobRepository)
    ) -> None:
        super().__init__(job_repository)
        self.itpro_partners_repository = itpro_partners_repository
    
    async def execute(self, db: Session):
        itpro_partners_datas = await self.itpro_partners_repository.fetch_itpro_partners()
        
        titles = itpro_partners_datas['titles']
        links = itpro_partners_datas['links']
        tags = itpro_partners_datas['tags']
        prices = itpro_partners_datas['prices']
        shows = itpro_partners_datas['show']

        length = len(titles)
        
        await self.store(db=db, length=length, titles=titles, links=links, tags=tags, prices=prices, shows=shows)

