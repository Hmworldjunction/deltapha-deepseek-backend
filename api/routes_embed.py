from fastapi import APIRouter, HTTPException
from models.schemas import EmbedRequest
from services.deepseek_client import get_embedding

router = APIRouter()

@router.post("/")
def embed(request: EmbedRequest):
    try:
        response = get_embedding(request.text)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))