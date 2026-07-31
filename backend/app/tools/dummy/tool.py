"""
Dummy tool.
"""

from __future__ import annotations

from app.tools.base import BaseTool
from app.tools.context import ToolContext
from app.tools.models import ToolResult


class DummyTool(BaseTool):
    """
    Simple demonstration tool.
    """

    @property
    def name(self) -> str:
        return "dummy"

    @property
    def description(self) -> str:
        return "Dummy demonstration tool."

    async def execute(
        self,
        context: ToolContext,
    ) -> ToolResult:
        """
        Execute the dummy tool.
        """

        arguments = context.arguments or {}

        name = arguments.get(
            "name",
            "User",
        )

        return ToolResult(
            success=True,
            message=f"Hello {name}! ULTRA-Z Tool System is working.",
        )