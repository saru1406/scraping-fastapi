from fastapi import Depends
from sqlalchemy.orm import Session

from backend.repositories.job.job_repository import JobRepository
from backend.repositories.lancers.lancers_repository import LancersRepository
from backend.repositories.qdrant.qdrant_repository import QdrantRepository
from backend.services.vector_service import VectorService
from backend.usecase.crawler.crawler_base_usecase import CrawlerBaseUsecase


class StoreLnacersUsecase(CrawlerBaseUsecase):
    def __init__(
        self,
        lancers_repository: LancersRepository = Depends(LancersRepository),
        job_repository: JobRepository = Depends(JobRepository),
        qdrant_repository: QdrantRepository = Depends(QdrantRepository),
        vector_servise: VectorService = Depends(VectorService),
    ) -> None:
        self.lancers_repository = lancers_repository
        self.qdrant_repository = qdrant_repository
        self.vector_servise = vector_servise
        self.job_repository = job_repository

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

        # self.qdrant_repository.create_collection(collection_name="job_collection")
        # for lancers in fetch_lancers:
        #     title_show = f"案件名: {lancers.title}, 案件詳細: {lancers.show}, URL: {lancers.link}"
        #     vector = self.vector_servise.create_vector(title_show)
        #     self.qdrant_repository.store_qdrant(lancers.id, vector, lancers.title, lancers.show, lancers.link)
