"""
Base runtime definition.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from app.runtime.state import RuntimeState
from app.runtime.metadata import RuntimeMetadata
from datetime import UTC, datetime

from app.runtime.health import RuntimeHealth

class Runtime(ABC):
    """
    Base runtime class.
    """
    @property
    def name(self) -> str:
        return self.metadata.name
    def __init__(
        self,
        metadata: RuntimeMetadata,
    ) -> None:

        self.metadata = metadata

        self.state = RuntimeState.CREATED

    @abstractmethod
    async def start(self) -> None:
        """
        Start the runtime.
        """
        raise NotImplementedError

    @abstractmethod
    async def stop(self) -> None:
        """
        Stop the runtime.
        """
        raise NotImplementedError

    async def health_check(self) -> RuntimeHealth:
        """
        Return runtime health information.
        """

        return RuntimeHealth(
            name=self.name,
            healthy=self.state == RuntimeState.RUNNING,
            state=self.state,
            checked_at=datetime.now(UTC),
            message="OK",
        )