from sqlalchemy.orm import Session
from fastapi import Depends

from app.repositories.lancers.lancers_repository import LancersRepository
from app.repositories.scraping.scraping_repository import ScrapingRepository
from app.usecase.crawler.crawler_base_usecase import CrawlerBaseUsecase

class StoreLnacersUsecase(CrawlerBaseUsecase):
    def __init__(
        self,
        lancers_repository: LancersRepository = Depends(LancersRepository),
        scraping_repository: ScrapingRepository = Depends(ScrapingRepository)
    ) -> None:
        super().__init__(scraping_repository)
        self.lancers_repository = lancers_repository
    
    async def execute(self, db: Session):
        lancers_dates = await self.lancers_repository.fetch_lancers()
        
        titles = lancers_dates['titles']
        links = lancers_dates['links']
        tags = lancers_dates['tags']
        prices = lancers_dates['prices']
        shows = lancers_dates['show']
        limits = lancers_dates['limits']

        length = len(titles)
        
        await self.store(db, length, titles=titles, links=links, tags=tags, prices=prices, shows=shows, limits=limits)
