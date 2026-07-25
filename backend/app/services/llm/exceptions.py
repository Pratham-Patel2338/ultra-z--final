"""
LLM exceptions.
"""


class LLMError(Exception):
    """Base exception."""


class LLMConnectionError(LLMError):
    """Connection failed."""


class LLMTimeoutError(LLMError):
    """Request timed out."""


class ModelNotAvailableError(LLMError):
    """Configured model is unavailable."""