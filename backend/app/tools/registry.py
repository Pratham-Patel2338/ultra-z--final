"""
Tool registry.
"""

from __future__ import annotations

from app.tools.base import BaseTool
from app.tools.exceptions import (
    DuplicateToolError,
    ToolNotFoundError,
)


class ToolRegistry:
    """
    Stores every registered tool.
    """

    def __init__(self) -> None:

        self._tools: dict[str, BaseTool] = {}

    def register(
        self,
        tool: BaseTool,
    ) -> None:
        """
        Register a tool.
        """

        if tool.name in self._tools:
            raise DuplicateToolError(tool.name)

        self._tools[tool.name] = tool

    def get(
        self,
        tool_name: str,
    ) -> BaseTool:
        """
        Return a registered tool.
        """

        tool = self._tools.get(tool_name)

        if tool is None:
            raise ToolNotFoundError(tool_name)

        return tool

    def exists(
        self,
        tool_name: str,
    ) -> bool:
        """
        Check whether a tool exists.
        """

        return tool_name in self._tools

    def list_tools(
        self,
    ) -> list[BaseTool]:
        """
        Return all registered tools.
        """

        return list(self._tools.values())

    def count(
        self,
    ) -> int:
        """
        Return number of registered tools.
        """

        return len(self._tools)
    
    def clear(self) -> None:
        """
        Remove all registered tools.
        """

        self._tools.clear()