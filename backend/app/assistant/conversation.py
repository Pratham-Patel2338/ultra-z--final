"""
Conversation object.
"""

from __future__ import annotations

from app.assistant.message import Message
from app.services.llm.chat import chat_service
from app.services.llm.types import ChatMessage, ChatResponse


class Conversation:
    """
    Represents a single conversation.
    """

    def __init__(
        self,
        system_prompt: str | None = None,
    ) -> None:

        self._messages: list[Message] = []

        if system_prompt:

            self.add_system(system_prompt)

    @property
    def messages(self) -> list[Message]:
        """
        Return conversation history.
        """

        return self._messages

    def add_system(
        self,
        content: str,
    ) -> None:

        self._messages.append(
            Message(
                role="system",
                content=content,
            )
        )

    def add_user(
        self,
        content: str,
    ) -> None:

        self._messages.append(
            Message(
                role="user",
                content=content,
            )
        )

    def add_assistant(
        self,
        content: str,
    ) -> None:

        self._messages.append(
            Message(
                role="assistant",
                content=content,
            )
        )

    async def ask(
        self,
        prompt: str,
    ) -> ChatResponse:
        """
        Send a message while preserving conversation history.
        """

        self.add_user(prompt)

        response = await chat_service.generate(
            [
                ChatMessage(
                    role=message.role,
                    content=message.content,
                )
                for message in self._messages
            ]
        )

        self.add_assistant(response.text)

        return response