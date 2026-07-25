"""
LLM chat service.
"""

from __future__ import annotations

from ollama import ResponseError

from app.core.logger import logger
from app.services.llm.client import llm_client
from app.services.llm.exceptions import (
    LLMConnectionError,
    ModelNotAvailableError,
)
from app.services.llm.models import model_manager
from app.services.llm.types import ChatResponse


class ChatService:
    """
    Handles conversations with the language model.
    """

    async def generate(
        self,
        prompt: str,
        system_prompt: str | None = None,
    ) -> ChatResponse:
        """
        Generate a response from the configured language model.
        """

        logger.info("=" * 60)
        logger.info("Starting chat generation...")

        model = await model_manager.get_chat_model()

        logger.info("Using model: %s", model)

        messages: list[dict[str, str]] = []

        logger.info("Building messages...")

        if system_prompt:
            messages.append(
                {
                    "role": "system",
                    "content": system_prompt,
                }
            )

        messages.append(
            {
                "role": "user",
                "content": prompt,
            }
        )

        logger.info("Messages built successfully.")
        logger.info("Sending request to Ollama...")

        try:
            response = await llm_client.client.chat(
                model=model,
                messages=messages,
            )

            logger.info("Received response from Ollama.")

        except ResponseError as exc:
            logger.exception("Ollama returned an error.")
            raise ModelNotAvailableError(str(exc)) from exc

        except Exception as exc:
            logger.exception("Failed while communicating with Ollama.")
            raise LLMConnectionError(str(exc)) from exc

        logger.info("Creating ChatResponse object...")

        chat_response = ChatResponse(
            text=response.message.content,
            model=model,
            prompt_tokens=getattr(response, "prompt_eval_count", None),
            completion_tokens=getattr(response, "eval_count", None),
            total_tokens=None,
        )

        logger.info("Chat generation completed successfully.")
        logger.info("=" * 60)

        return chat_response


chat_service = ChatService()