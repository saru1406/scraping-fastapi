from fastapi import Depends

from backend.repositories.qdrant.qdrant_repository import QdrantRepository
from backend.services.vector_service import VectorService


class CreatePrompt:
    def __init__(
        self,
        vector_servise: VectorService = Depends(VectorService),
        qdrant_repository: QdrantRepository = Depends(QdrantRepository),
    ) -> None:
        self.vector_servise = vector_servise
        self.qdrant_repository = qdrant_repository

    def create_prompt(self, text: str):
        vector = self.vector_servise.create_vector(text)
        self.qdrant_repository.store_qdrant(vector, text)
