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
            model="gpt-3.5-turbo",
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
                    "description": "個人情報に関してを提供します",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "text": {
                                "type": "string",
                                "description": "個人情報に関して",
                            }
                        },
                        "required": ["text"],
                    },
                }
            ],
            function_call={
                "name": "search_qdrant",
                "arguments": {"text": "motivation"},
            },
        )
        print(response.choices[0].message.function_call.name)
        return response.choices[0].message

    def fetch_rag_chat(self, text: str):
        open_ai = OpenAI(api_key=os.getenv("OPEN_AI"))
        response = open_ai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "ユーザーの質問に対して親切にサポートを提供してください。",
                },
                {"role": "user", "content": text},
            ],
        )
        return response.choices[0].message.content
