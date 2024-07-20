import os

from fastapi import Depends
from openai import OpenAI


class OpenAiReposiotry:
    # def __init__(self, open_ai: OpenAI = Depends(OpenAI)) -> None:
    #     self.open_ai = open_ai
    #     self.open_ai.api_key = os.getenv("Open_AI")

    def fetch_farst_chat(self, text: str):
        open_ai = OpenAI(api_key=os.getenv("OPEN_AI"))
        response = open_ai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "ユーザーの質問に対して親切にサポートを提供してください。",
                },
                {"role": "user", "content": text},
            ],
            functions=[
                {
                    "name": "search_qdrant",
                    "description": "フリーランス・副業案件について提供します",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "text": {
                                "type": "string",
                                "description": "フリーランス・副業案件について提供します",
                            }
                        },
                        "required": ["text"],
                    },
                }
            ],
        )
        print(response.choices[0].message)
        return response.choices[0].message

    def fetch_rag_chat(self, text: str, db_response):
        open_ai = OpenAI(api_key=os.getenv("OPEN_AI"))
        response = open_ai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": f"以下はデータベースから取得した情報です。\n {db_response} \n これを元にユーザーの質問に答えてください。URLは必ず表示させてください。",
                },
                {"role": "user", "content": text},
                # {"role": "assistant", "content": db_response},
            ],
        )
        print(response.choices)
        return response.choices[0].message.content
