from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # API Keys
    deepseek_api_key: Optional[str] = None
    openai_api_key: Optional[str] = None
    
    # Model Settings
    max_tokens: int = 2000
    temperature: float = 0.7
    top_p: float = 0.95
    
    # Service Settings
    service_name: str = "assignment-ai-service"
    version: str = "1.0.0"
    
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()
