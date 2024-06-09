from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from typing import List, Optional

from app.repositories.scraping.scraping_repository import ScrapingRepository
from app.models.job import Job

class CrawlerBaseUsecase(ABC):
    def __init__(self, scraping_repository: ScrapingRepository) -> None:
        self.scraping_repository = scraping_repository
    
    async def store(
        self,
        db: Session,
        length: int,
        titles: List[str] = None,
        links: List[str] = None,
        tags: Optional[List[str]] = None,
        prices: Optional[List[str]] = None,
        shows: Optional[List[str]] = None,
        limits: Optional[List[str]] = None
    ):
        chunk_size = 1000
        for i in range(0, length, chunk_size):
            chunk_titles = titles[i:i + chunk_size]
            chunk_links = links[i:i + chunk_size]
            chunk_tags = tags[i:i + chunk_size] if tags else None
            chunk_prices = prices[i:i + chunk_size] if prices else None
            chunk_shows = shows[i:i + chunk_size] if shows else None
            chunk_limit = limits[i:i + chunk_size] if limits else None

            job_objects = [
                Job(
                    title=chunk_titles[j],
                    link=chunk_links[j],
                    tags=chunk_tags[j],
                    show=chunk_shows[j],
                    price=chunk_prices[j],
                    limit=chunk_limit[j] if chunk_limit else None
                )
                for j in range(len(chunk_titles))
            ]

            await self.scraping_repository.store(db, job_objects)
            