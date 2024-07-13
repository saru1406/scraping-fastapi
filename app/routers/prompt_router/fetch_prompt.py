from fastapi import APIRouter, Depends

from app.schemas.prompt_schema import PromptSchema
from app.usecase.prompt.fetch_prompt import FetchPrompt

router = APIRouter()


@router.post("/prompts", tags=["prompt"])
def fetch_prompt(
    request: PromptSchema, prompt_usecase: FetchPrompt = Depends(FetchPrompt)
):
    return prompt_usecase.fetch(request.text)
