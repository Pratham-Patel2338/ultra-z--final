"""
Shared LLM data types.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class ChatMessage:
    """
    A single chat message.
    """

    role: str
    content: str


@dataclass(slots=True)
class ChatResponse:
    """
    Response returned by the chat service.
    """

    text: str

    model: str

    prompt_tokens: int | None = None

    completion_tokens: int | None = None

    total_tokens: int | None = None