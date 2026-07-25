"""
Application settings.
"""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""

    app_name: str = "ULTRA-Z"
    app_version: str = "1.0.0"
    debug: bool = True

    host: str = "127.0.0.1"
    port: int = 8000

    api_prefix: str = "/api/v1"
    
    
    


    ollama_host: str = "http://localhost:11434"

    ollama_timeout: int = 300

    default_chat_model: str = "qwen3:8b"

    default_embedding_model: str = "nomic-embed-text:latest"

    # -------------------------
    # Database
    # -------------------------

    database_url: str = "sqlite+aiosqlite:///storage/database/ultra_z.db"
    database_echo: bool = False

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


@lru_cache
def get_settings() -> Settings:
    """Return a cached Settings instance."""
    return Settings()

settings = get_settings()