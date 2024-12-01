import concurrent.futures

from fastapi import Depends
from sqlalchemy.orm import Session

from backend.models.job import Job
from backend.repositories.custom.custom_repository import CustomRepository
from backend.repositories.qdrant.qdrant_repository import QdrantRepository
from backend.services.vector_service import VectorService


class StoreCustomUsecase:
    def __init__(
        self,
        custom_repository: CustomRepository = Depends(CustomRepository),
        vector_servise: VectorService = Depends(VectorService),
        qdrant_repository: QdrantRepository = Depends(QdrantRepository),
    ) -> None:
        self.job_repository = custom_repository
        self.vector_servise = vector_servise
        self.qdrant_repository = qdrant_repository
        
    async def execute(self, db: Session):
        pass
        

    async def store_qdrant_by_job(self, db: Session):
        jobs = self.job_repository.fetch(db=db)
        await self.qdrant_repository.create_collection(collection_name="job_collection")
        await self.concurrent_vector(jobs)

    async def concurrent_vector(self, jobs: list[Job]):
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
            list(executor.map(await self.process_job, jobs))

    async def process_job(self, job: Job):
        title_show = f"案件名: {job.title}, 案件詳細: {job.show}, URL: {job.link}"
        vector = self.vector_servise.create_vector(title_show)
        await self.qdrant_repository.store_qdrant(
            job.id,
            vector,
            job.title,
            job.show,
            job.link,
        )
