"""
LLM model management.
"""

from __future__ import annotations

from dataclasses import dataclass

from app.core.logger import logger
from app.core.settings import settings
from app.services.llm.client import llm_client


@dataclass(slots=True)
class LLMModel:
    """
    Represents an installed LLM model.
    """

    name: str
    size: int | None = None
    modified_at: str | None = None


class ModelManager:
    """
    Manages installed language models.
    """

    async def list_models(self) -> list[LLMModel]:
        """
        Return all installed models.
        """

        response = await llm_client.client.list()

        models: list[LLMModel] = []

        for model in response.models:

            models.append(
                LLMModel(
                    name=model.model,
                    size=getattr(model, "size", None),
                    modified_at=str(getattr(model, "modified_at", "")),
                )
            )

        return models

    async def model_exists(
        self,
        model_name: str,
    ) -> bool:
        """
        Check whether a model exists.
        """

        models = await self.list_models()

        return any(model.name == model_name for model in models)

    async def get_chat_model(self) -> str:
        """
        Return the configured chat model.
        """

        exists = await self.model_exists(
            settings.default_chat_model
        )

        if not exists:
            raise RuntimeError(
                f"Chat model '{settings.default_chat_model}' is not installed."
            )

        

        return settings.default_chat_model

    async def get_embedding_model(self) -> str:
        """
        Return the configured embedding model.
        """

        exists = await self.model_exists(
            settings.default_embedding_model
        )

        if not exists:
            raise RuntimeError(
                f"Embedding model '{settings.default_embedding_model}' is not installed."
            )

        logger.info(
            "Using embedding model: %s",
            settings.default_embedding_model,
        )

        return settings.default_embedding_model


model_manager = ModelManager()