"""
Assistant exceptions.
"""


class ConversationNotFoundError(Exception):
    """
    Raised when a conversation cannot be found.
    """

    def __init__(self, conversation_id: str) -> None:
        super().__init__(
            f"Conversation '{conversation_id}' does not exist."
        )