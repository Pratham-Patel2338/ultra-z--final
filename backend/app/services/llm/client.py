"""
LLM client interface.
"""

from __future__ import annotations

from ollama import AsyncClient

from app.core.settings import settings


class LLMClient:
    """
    Base client for communicating with the configured LLM provider.
    """

    def __init__(self) -> None:
        self._client = AsyncClient(
            host=settings.ollama_host,
        )

    @property
    def client(self) -> AsyncClient:
        """
        Return the underlying provider client.
        """
        return self._client


llm_client = LLMClient()