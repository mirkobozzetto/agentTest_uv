from pydantic_settings import BaseSettings
from pydantic import SecretStr, Field
from typing import Optional, List


class Settings(BaseSettings):
    """Configuration for the agent."""

    openai_api_key: SecretStr = Field(..., env="OPENAI_API_KEY")
    model: str = "gpt-4.1-mini-2025-04-14"
    temperature: float = 0.7
    max_tokens: Optional[int] = None
    top_p: float = 1.0
    frequency_penalty: float = 0.0
    presence_penalty: float = 0.0
    stop: Optional[List[str]] = None
    timeout: int = 30

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
