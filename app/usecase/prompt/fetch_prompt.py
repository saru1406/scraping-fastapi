from fastapi import Depends

from app.repositories.qdrant.qdrant_repository import QdrantRepository
from app.services.vector_service import VectorService


class FetchPrompt:
    def __init__(
        self,
        qdrant_repository: QdrantRepository = Depends(QdrantRepository),
        vector_service: VectorService = Depends(VectorService),
    ) -> None:
        self.qdrant_repository = qdrant_repository
        self.vector_service = vector_service

    def fetch(self, text: str):
        vector = self.vector_service.create_vector(text)
        return self.qdrant_repository.search_qdrant(vector)
