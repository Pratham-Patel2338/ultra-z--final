"""
LLM health service.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime

from ollama import ResponseError

from app.services.llm.client import llm_client


@dataclass(slots=True)
class LLMHealth:
    """
    Health information for the LLM provider.
    """

    healthy: bool

    checked_at: datetime

    message: str

    model_count: int = 0


class LLMHealthService:
    """
    Performs health checks for the configured LLM.
    """

    async def check(self) -> LLMHealth:

        try:

            response = await llm_client.client.list()

            models = response.models

            return LLMHealth(
                healthy=True,
                checked_at=datetime.now(UTC),
                message="Connected",
                model_count=len(models),
            )

        except ResponseError as exc:

            return LLMHealth(
                healthy=False,
                checked_at=datetime.now(UTC),
                message=str(exc),
            )

        except Exception as exc:

            return LLMHealth(
                healthy=False,
                checked_at=datetime.now(UTC),
                message=str(exc),
            )


llm_health = LLMHealthService()