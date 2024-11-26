from pydantic import BaseModel


class PromptSchema(BaseModel):
    text: str
