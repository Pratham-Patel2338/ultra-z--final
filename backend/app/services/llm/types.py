"""
Shared LLM data types.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class ChatMessage:
    """
    Represents one message in a conversation.
    """

    role: str
    content: str


@dataclass(slots=True)
class ChatChunk:
    """
    One streamed chunk from the LLM.
    """

    text: str

    done: bool = False


@dataclass(slots=True)
class ChatResponse:
    """
    Final response returned by ChatService.generate().
    """

    text: str

    model: str

    prompt_tokens: int | None = None

    completion_tokens: int | None = None

    total_tokens: int | None = None