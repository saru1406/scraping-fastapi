from fastapi import Depends
from sqlalchemy.orm import Session

from app.repositories.job.job_repository import JobRepository
from app.repositories.lancers.lancers_repository import LancersRepository
from app.usecase.crawler.crawler_base_usecase import CrawlerBaseUsecase
from app.repositories.qdrant.qdrant_repository import QdrantRepository
from app.services.vector_service import VectorService


class StoreLnacersUsecase(CrawlerBaseUsecase):
    def __init__(
        self,
        lancers_repository: LancersRepository = Depends(LancersRepository),
        job_repository: JobRepository = Depends(JobRepository),
        qdrant_repository: QdrantRepository = Depends(QdrantRepository),
        vector_servise: VectorService = Depends(VectorService),
    ) -> None:
        super().__init__(job_repository)
        self.lancers_repository = lancers_repository
        self.qdrant_repository = qdrant_repository
        self.vector_servise = vector_servise

    async def execute(self, db: Session):
        lancers_dates = await self.lancers_repository.fetch_lancers()

        titles = lancers_dates["titles"]
        links = lancers_dates["links"]
        tags = lancers_dates["tags"]
        prices = lancers_dates["prices"]
        shows = lancers_dates["show"]
        limits = lancers_dates["limits"]

        length = len(titles)

        await self.store(
            db=db,
            length=length,
            titles=titles,
            links=links,
            tags=tags,
            prices=prices,
            shows=shows,
            limits=limits,
        )
        
        id = 1
        for title in titles:
            vector_title = self.vector_servise.create_vector(title)
            self.qdrant_repository.store_qdrant(id, vector_title, title)
            id += 1

        
