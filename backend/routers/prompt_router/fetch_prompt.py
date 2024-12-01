from fastapi import APIRouter, Depends

from backend.repositories.open_ai.open_ai_repository import OpenAiRepository
from backend.schemas.prompt_schema import PromptSchema
from backend.usecase.prompt.fetch_prompt import FetchPrompt

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
    open_ai_repository: OpenAiRepository = Depends(OpenAiRepository),
):
    return open_ai_repository.fetch_farst_chat(request.text)
