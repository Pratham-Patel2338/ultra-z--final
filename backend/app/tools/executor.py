"""
Tool executor.
"""

from __future__ import annotations

from app.tools.context import ToolContext
from app.tools.exceptions import ToolExecutionError
from app.tools.manager import tool_manager
from app.tools.models import ToolResult


class ToolExecutor:
    """
    Executes registered tools.
    """

    async def execute(
        self,
        tool_name: str,
        context: ToolContext,
    ) -> ToolResult:
        """
        Execute a tool.
        """

        tool = tool_manager.get(tool_name)

        try:

            return await tool.execute(context)

        except Exception as exc:

            raise ToolExecutionError(
                tool_name,
                str(exc),
            ) from exc


tool_executor = ToolExecutor()