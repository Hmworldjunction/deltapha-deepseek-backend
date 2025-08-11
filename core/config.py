import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    api_key: str = os.getenv("DEEPSEEK_API_KEY")
    api_base: str = os.getenv("DEEPSEEK_API_BASE", "https://api.deepseek.com/v1")

def get_settings():
    return Settings()