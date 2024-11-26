from fastapi import Depends

from backend.repositories.open_ai.open_ai_repository import OpenAiReposiotry
from backend.repositories.qdrant.qdrant_repository import QdrantRepository
from backend.services.vector_service import VectorService


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
            qdrant_responses = self.qdrant_repository.search_qdrant(vector, 5)

            n = 1
            full_text = ""
            for qdrant_response in qdrant_responses:
                number = f"{n}件目 \n"
                title = f"案件名:{qdrant_response.payload['案件名']} \n"
                show = f"案件詳細:{qdrant_response.payload['案件詳細']} \n"
                url = f"URL:{qdrant_response.payload['URL']}"
                full_text += f"{number}{title}{show}\n{url}"

                n += 1

            print(full_text)

            if qdrant_response:
                return self.open_ai_repository.fetch_rag_chat(text, full_text)

        return response.content
