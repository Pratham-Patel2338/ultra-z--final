"""
Tool manager.
"""

from __future__ import annotations

from app.tools.base import BaseTool
from app.tools.registry import ToolRegistry


class ToolManager:
    """
    High-level interface for managing tools.
    """

    def __init__(self) -> None:
        self._registry = ToolRegistry()

    @property
    def registry(self) -> ToolRegistry:
        """
        Return the underlying registry.
        """
        return self._registry

    def register(
        self,
        tool: BaseTool,
    ) -> None:
        """
        Register a tool.
        """
        self._registry.register(tool)

    def get(
        self,
        tool_name: str,
    ) -> BaseTool:
        """
        Return a registered tool.
        """
        return self._registry.get(tool_name)

    def exists(
        self,
        tool_name: str,
    ) -> bool:
        """
        Check whether a tool exists.
        """
        return self._registry.exists(tool_name)

    def list_tools(
        self,
    ) -> list[BaseTool]:
        """
        Return all registered tools.
        """
        return self._registry.list_tools()

    def count(
        self,
    ) -> int:
        """
        Return number of registered tools.
        """
        return self._registry.count()

    def clear(
        self,
    ) -> None:
        """
        Remove all registered tools.
        """
        self._registry.clear()


tool_manager = ToolManager()