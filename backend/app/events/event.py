"""
Base event definitions for ULTRA-Z.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import Enum
from uuid import uuid4


class EventPriority(Enum):
    """
    Priority of an event.
    """

    LOW = 1
    NORMAL = 2
    HIGH = 3
    CRITICAL = 4


@dataclass(slots=True)
class Event:
    """
    Base event used throughout ULTRA-Z.
    """

    name: str

    payload: dict = field(default_factory=dict)

    source: str = "system"

    priority: EventPriority = EventPriority.NORMAL

    correlation_id: str | None = None

    event_id: str = field(default_factory=lambda: str(uuid4()))

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )