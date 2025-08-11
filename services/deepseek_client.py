import requests
from core.config import get_settings

settings = get_settings()

def query_deepseek(prompt):
    url = f"{settings.api_base}/chat/completions"
    headers = {"Authorization": f"Bearer {settings.api_key}"}
    payload = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

def get_embedding(text):
    url = f"{settings.api_base}/embeddings"
    headers = {"Authorization": f"Bearer {settings.api_key}"}
    payload = {"input": text, "model": "deepseek-embed"}
    response = requests.post(url, json=payload, headers=headers)
    return response.json()