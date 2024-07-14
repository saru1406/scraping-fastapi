from fastapi import APIRouter, Depends

from app.repositories.open_ai.open_ai_repository import OpenAiReposiotry
from app.schemas.prompt_schema import PromptSchema
from app.usecase.prompt.fetch_prompt import FetchPrompt

router = APIRouter()


@router.post("/prompts", tags=["prompt"])
def fetch_prompt(
    request: PromptSchema, prompt_usecase: FetchPrompt = Depends(FetchPrompt)
):
    response_gpt = prompt_usecase.fetch(request.text)
    return {"text": response_gpt}

@router.post("/chat", tags=["gpt"])
def fetch_chat(
    request: PromptSchema,
    open_ai_repository: OpenAiReposiotry = Depends(OpenAiReposiotry),
):
    return open_ai_repository.fetch_chat(request.text)
