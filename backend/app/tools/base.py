"""
Base class for all ULTRA-Z tools.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from app.tools.context import ToolContext
from app.tools.models import ToolResult

from app.tools.models import ToolInfo


class BaseTool(ABC):
    """
    Base class for every executable tool.
    """
    
    @property
    def info(self) -> ToolInfo:
        """
        Return tool metadata.
        """

        return ToolInfo(
            name=self.name,
            description=self.description,
            enabled=self.enabled,
        )

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Unique tool name.
        """

    @property
    def description(self) -> str:
        """
        Human-readable description.
        """

        return ""

    @property
    def enabled(self) -> bool:
        """
        Whether the tool is enabled.
        """

        return True

    @abstractmethod
    async def execute(
        self,
        context: ToolContext,
    ) -> ToolResult:
        """
        Execute the tool.
        """