from sqlalchemy.orm import Session
from fastapi import Depends
from app.repositories.itpro_partners.itpro_partners_repository import ItproPartnersRepository
from app.repositories.scraping.scraping_repository import ScrapingRepository
from app.models.job import Job

class StoreItproPartnersUsecase:
    def __init__(
        self,
        itpro_partners_repository: ItproPartnersRepository = Depends(ItproPartnersRepository),
        scraping_repository: ScrapingRepository = Depends(ScrapingRepository)
    ) -> None:
        self.itpro_partners_repository = itpro_partners_repository
        self.scraping_repository = scraping_repository
    
    async def execute(self, db: Session):
        itpro_partners_datas = await self.itpro_partners_repository.fetch_itpro_partners()
        
        titles = itpro_partners_datas['titles']
        links = itpro_partners_datas['links']
        tags = itpro_partners_datas['tags']
        prices = itpro_partners_datas['prices']
        shows = itpro_partners_datas['show']

        data_length = len(titles)
        
        # データを1000件ずつチャンクに分けて処理
        chunk_size = 1000
        for i in range(0, data_length, chunk_size):
            chunk_titles = titles[i:i + chunk_size]
            chunk_links = links[i:i + chunk_size]
            chunk_tags = tags[i:i + chunk_size]
            chunk_prices = prices[i:i + chunk_size]
            chunk_shows = shows[i:i + chunk_size]

            job_objects = [
                Job(
                    title=chunk_titles[j],
                    link=chunk_links[j],
                    tags=chunk_tags[j],
                    show=chunk_shows[j],
                    price=chunk_prices[j],
                    limit=None
                )
                for j in range(len(chunk_titles))
            ]

            self.scraping_repository.store(db, job_objects)
    