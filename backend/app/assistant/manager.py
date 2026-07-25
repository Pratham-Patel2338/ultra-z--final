"""
Conversation manager.
"""

from __future__ import annotations

from uuid import uuid4

from app.assistant.conversation import Conversation

from app.assistant.exceptions import ConversationNotFoundError


class ConversationManager:
    """
    Manages active conversations.
    """

    def __init__(self) -> None:

        self._conversations: dict[str, Conversation] = {}

    def create(
        self,
        system_prompt: str | None = None,
    ) -> str:
        """
        Create a new conversation.

        Returns:
            Conversation ID.
        """

        conversation_id = str(uuid4())

        self._conversations[conversation_id] = Conversation(
            system_prompt=system_prompt,
        )

        return conversation_id

    def get(
        self,
        conversation_id: str,
    ) -> Conversation:
        """
        Get an existing conversation.
        """

        conversation = self._conversations.get(conversation_id)

        if conversation is None:
            raise ConversationNotFoundError(conversation_id)

        return conversation

    def exists(
        self,
        conversation_id: str,
    ) -> bool:
        """
        Check whether a conversation exists.
        """

        return conversation_id in self._conversations

    def delete(
        self,
        conversation_id: str,
    ) -> None:
        """
        Delete a conversation.
        """

        if conversation_id not in self._conversations:
            raise ConversationNotFoundError(conversation_id)

        del self._conversations[conversation_id]

    def list_ids(
        self,
    ) -> list[str]:
        """
        Return all conversation IDs.
        """

        return list(self._conversations.keys())

    def count(
        self,
    ) -> int:
        """
        Return number of active conversations.
        """

        return len(self._conversations)


conversation_manager = ConversationManager()