from fastapi import FastAPI, Depends, HTTPException
from api.routes_chat import router as chat_router
from api.routes_generate import router as generate_router
from api.routes_embed import router as embed_router
from core.config import get_settings

app = FastAPI(title="Deltapha DeepSeek API")

app.include_router(chat_router, prefix="/chat")
app.include_router(generate_router, prefix="/generate")
app.include_router(embed_router, prefix="/embed")

@app.get("/health")
def health_check():
    return {"status": "ok"}