from pydantic import BaseModel

class PromptSchema(BaseModel):
    text: list[object]
