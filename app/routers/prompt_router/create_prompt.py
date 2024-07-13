from fastapi import APIRouter, Depends

from app.database import get_db
from app.schemas.prompt_schema import PromptSchema
from app.usecase.prompt.create_prompt import CreatePrompt

router = APIRouter()


@router.post("/prompt", tags=["prompt"])
def prompt(request: PromptSchema, prompt_usecase: CreatePrompt = Depends(CreatePrompt)):
    prompt_usecase.create_prompt(request.text)
    return "成功"
