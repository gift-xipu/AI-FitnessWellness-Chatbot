from pydantic_settings import BaseSettings
from functools import lru_cache
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    # API Keys
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    
    # API Configuration
    MODEL_NAME: str = "gpt-3.5-turbo"
    TEMPERATURE: float = 0.7
    MAX_TOKENS: int = 150
    
    # Chat Modes
    AVAILABLE_MODES: list[str] = ["fitness", "mindfulness", "recipe", "general"]
    
    # Logging
    LOG_LEVEL: str = "INFO"

    class Config:
        case_sensitive = True

@lru_cache()
def get_settings():
    return Settings()

# Create a settings instance
settings = get_settings()