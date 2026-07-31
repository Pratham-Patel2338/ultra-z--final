"""
Tool execution context.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class ToolContext:
    """
    Context shared with every tool execution.
    """

    conversation_id: str | None = None

    user_input: str = ""

    arguments: dict[str, Any] | None = None