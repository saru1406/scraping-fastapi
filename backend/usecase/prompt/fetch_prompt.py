from fastapi import Depends

from backend.repositories.open_ai.open_ai_repository import OpenAiRepository
from backend.repositories.qdrant.qdrant_repository import QdrantRepository
from backend.services.vector_service import VectorService
import json


class FetchPrompt:
    def __init__(
        self,
        qdrant_repository: QdrantRepository = Depends(QdrantRepository),
        vector_service: VectorService = Depends(VectorService),
        open_ai_repository: OpenAiRepository = Depends(OpenAiRepository),
    ) -> None:
        self.qdrant_repository = qdrant_repository
        self.vector_service = vector_service
        self.open_ai_repository = open_ai_repository

    def fetch(self, text: list[object]) -> str:
        messages = [
        {"role": "system", "content": "ユーザーの質問に対して親切にサポートを提供してください。"}
    ] + [{"role": t["role"], "content": t["text"]} for t in text]
        response = self.open_ai_repository.fetch_farst_chat(messages)
        print(response.function_call)
        if response.function_call:
            print(json.loads(response.function_call.arguments).get("text"))
            # print(response.function_call["text"])
            response_text = json.loads(response.function_call.arguments).get("text")
            vector = self.vector_service.create_vector(response_text)
            qdrant_responses = self.qdrant_repository.search_qdrant(vector, 5)

            n = 1
            full_text = ""
            for qdrant_response in qdrant_responses:
                number = f"{n}件目 \n"
                title = f"案件名:{qdrant_response.payload['案件名']} \n"
                show = f"案件詳細:{qdrant_response.payload['案件詳細']} \n"
                url = f"URL:{qdrant_response.payload['URL']} \n"
                full_text += f"{number}{title}{show}\n{url}"
                print(url)

                n += 1

            print(full_text)

            if qdrant_response:
                messages.append({
                    "role": "system",
                    "content": f"以下はデータベースから取得した情報です。\n {full_text} \n これを元にユーザーの質問に答えてください。URLは必ず表示させてください。"
                })

                return self.open_ai_repository.fetch_rag_chat(messages)

        return response.content
