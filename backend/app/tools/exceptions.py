"""
Tool system exceptions.
"""


class ToolError(Exception):
    """
    Base exception for all tool-related errors.
    """


class ToolNotFoundError(ToolError):
    """
    Raised when a requested tool does not exist.
    """

    def __init__(self, tool_name: str) -> None:
        super().__init__(
            f"Tool '{tool_name}' does not exist."
        )


class DuplicateToolError(ToolError):
    """
    Raised when registering a tool that already exists.
    """

    def __init__(self, tool_name: str) -> None:
        super().__init__(
            f"Tool '{tool_name}' is already registered."
        )


class ToolExecutionError(ToolError):
    """
    Raised when a tool fails during execution.
    """

    def __init__(
        self,
        tool_name: str,
        message: str,
    ) -> None:
        super().__init__(
            f"Tool '{tool_name}' failed: {message}"
        )