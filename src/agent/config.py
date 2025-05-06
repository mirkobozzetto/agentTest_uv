from pydantic_settings import BaseSettings
from pydantic import SecretStr, Field


class Settings(BaseSettings):
    """Configuration for the agent."""

    openai_api_key: SecretStr = Field(..., env="OPENAI_API_KEY")
    model: str = "gpt-4.1-mini-2025-04-14"
    temperature: float = 0.7

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
