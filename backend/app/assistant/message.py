"""
Conversation message model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Message:
    """
    Represents one conversation message.
    """

    role: str
    content: str