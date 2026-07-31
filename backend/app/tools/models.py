"""
Tool data models.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class ToolResult:
    """
    Result returned by a tool execution.
    """

    success: bool
    message: str = ""
    data: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class ToolInfo:
    """
    Metadata describing a tool.
    """

    name: str
    description: str
    enabled: bool = True