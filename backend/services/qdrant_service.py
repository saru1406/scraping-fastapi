from fastapi import Depends

from backend.repositories.qdrant.qdrant_repository import QdrantRepository


class QdrantService:
    def __init__(
        self, qdrant_repository: QdrantRepository = Depends(QdrantRepository)
    ) -> None:
        self.qdrant_repository = qdrant_repository

    def create_qdrant_collection(self):
        self.qdrant_repository.create_collection(collection_name="job_collection")
