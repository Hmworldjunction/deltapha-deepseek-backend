from fastapi import APIRouter, HTTPException
from models.schemas import PromptRequest
from services.deepseek_client import query_deepseek

router = APIRouter()

@router.post("/")
def generate(request: PromptRequest):
    try:
        response = query_deepseek(request.prompt)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))