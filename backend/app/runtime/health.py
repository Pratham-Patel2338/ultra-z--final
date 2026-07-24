"""
Runtime health monitoring.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime

from app.runtime.state import RuntimeState


@dataclass(slots=True)
class RuntimeHealth:
    """
    Health information for a runtime.
    """

    name: str

    healthy: bool

    state: RuntimeState

    checked_at: datetime

    message: str = ""