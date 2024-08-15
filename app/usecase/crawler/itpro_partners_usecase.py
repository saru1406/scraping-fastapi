from fastapi import Depends
from sqlalchemy.orm import Session

from app.repositories.itpro_partners.itpro_partners_repository import \
    ItproPartnersRepository
from app.repositories.job.job_repository import JobRepository
from app.repositories.qdrant.qdrant_repository import QdrantRepository
from app.services.vector_service import VectorService
from app.usecase.crawler.crawler_base_usecase import CrawlerBaseUsecase


class StoreItproPartnersUsecase(CrawlerBaseUsecase):
    def __init__(
        self,
        itpro_partners_repository: ItproPartnersRepository = Depends(
            ItproPartnersRepository
        ),
        job_repository: JobRepository = Depends(JobRepository),
        qdrant_repository: QdrantRepository = Depends(QdrantRepository),
        vector_servise: VectorService = Depends(VectorService),
    ) -> None:
        self.itpro_partners_repository = itpro_partners_repository
        self.qdrant_repository = qdrant_repository
        self.vector_servise = vector_servise
        self.job_repository = job_repository

    async def execute(self, db: Session):
        itpro_partners_datas = (
            await self.itpro_partners_repository.fetch_itpro_partners()
        )

        titles = itpro_partners_datas["titles"]
        links = itpro_partners_datas["links"]
        tags = itpro_partners_datas["tags"]
        prices = itpro_partners_datas["prices"]
        shows = itpro_partners_datas["show"]

        length = len(titles)

        await self.store(
            db=db,
            length=length,
            titles=titles,
            links=links,
            tags=tags,
            prices=prices,
            shows=shows,
        )

        # self.qdrant_repository.create_collection(collection_name="job_collection")
        # for itpro_partners in fetch_itpro_partners:
        #     title_show = f"案件名: {itpro_partners.title}, 案件詳細: {itpro_partners.show}, URL: {itpro_partners.link}"
        #     vector = self.vector_servise.create_vector(title_show)
        #     self.qdrant_repository.store_qdrant(itpro_partners.id, vector, itpro_partners.title, itpro_partners.show, itpro_partners.link)
