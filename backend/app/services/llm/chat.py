"""
LLM chat service.
"""

from __future__ import annotations

from collections.abc import AsyncGenerator

from ollama import ResponseError

from app.core.logger import logger
from app.services.llm.client import llm_client
from app.services.llm.exceptions import (
    LLMConnectionError,
    ModelNotAvailableError,
)
from app.services.llm.models import model_manager
from app.services.llm.types import (
    ChatChunk,
    ChatMessage,
    ChatResponse,
)


class ChatService:
    """
    Handles conversations with the language model.
    """

    async def stream(
        self,
        messages: list[ChatMessage],
        model: str,
    ) -> AsyncGenerator[ChatChunk, None]:
        """
        Stream a response from the LLM.
        """

        

        logger.info("Streaming response...")

        ollama_messages = [
            {
                "role": message.role,
                "content": message.content,
            }
            for message in messages
        ]

        try:

            stream = await llm_client.client.chat(
                model=model,
                messages=ollama_messages,
                stream=True,
            )

            async for part in stream:

                text = part.message.content or ""

                if text:

                    yield ChatChunk(
                        text=text,
                        done=False,
                    )

            yield ChatChunk(
                text="",
                done=True,
            )

            logger.info("Response received.")

        except ResponseError as exc:

            raise ModelNotAvailableError(str(exc)) from exc

        except Exception as exc:

            raise LLMConnectionError(str(exc)) from exc

    async def generate(
        self,
        messages: list[ChatMessage],
    ) -> ChatResponse:
        """
        Generate the complete response.
        """

        logger.info("=" * 60)
        logger.info("Starting chat generation...")

        model = await model_manager.get_chat_model()

        logger.info("Using model: %s", model)

        complete_text = ""

        async for chunk in self.stream(
            messages=messages,
            model=model,
        ):
            complete_text += chunk.text

        logger.info("Chat generation completed.")
        logger.info("=" * 60)

        return ChatResponse(
            text=complete_text,
            model=model,
        )


chat_service = ChatService()