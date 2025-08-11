from pydantic import BaseModel

class PromptRequest(BaseModel):
    prompt: str

class EmbedRequest(BaseModel):
    text: str