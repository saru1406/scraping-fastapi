import os

from fastapi import Depends
from openai import OpenAI


class OpenAiRepository:
    # def __init__(self, open_ai: OpenAI = Depends(OpenAI)) -> None:
    #     self.open_ai = open_ai
    #     self.open_ai.api_key = os.getenv("Open_AI")

    def fetch_farst_chat(self, messages: list[object]):
        open_ai = OpenAI(api_key=os.getenv("OPEN_AI"))
        response = open_ai.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
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
        # print(response.choices[0].message)
        return response.choices[0].message

    def fetch_rag_chat(self, messages: list[object]):
        open_ai = OpenAI(api_key=os.getenv("OPEN_AI"))
        response = open_ai.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
        )
        print(response.choices)
        return response.choices[0].message.content
