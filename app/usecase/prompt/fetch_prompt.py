from fastapi import Depends

from app.repositories.open_ai.open_ai_repository import OpenAiReposiotry
from app.repositories.qdrant.qdrant_repository import QdrantRepository
from app.services.vector_service import VectorService


class FetchPrompt:
    def __init__(
        self,
        qdrant_repository: QdrantRepository = Depends(QdrantRepository),
        vector_service: VectorService = Depends(VectorService),
        open_ai_repository: OpenAiReposiotry = Depends(OpenAiReposiotry),
    ) -> None:
        self.qdrant_repository = qdrant_repository
        self.vector_service = vector_service
        self.open_ai_repository = open_ai_repository

    def fetch(self, text: str) -> str:
        response = self.open_ai_repository.fetch_farst_chat(text)
        print(response.function_call)
        if response.function_call:
            vector = self.vector_service.create_vector(text)
            qdrant_response = self.qdrant_repository.search_qdrant(vector, 1)
            print(qdrant_response[0].payload['name'])
            if qdrant_response:
                return self.open_ai_repository.fetch_rag_chat(text, qdrant_response[0].payload['name'])

        return response.content
