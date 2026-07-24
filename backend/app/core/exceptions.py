"""
Custom exceptions used throughout the ULTRA-Z application.
"""

from __future__ import annotations


class UltraZException(Exception):
    """
    Base exception for all ULTRA-Z exceptions.
    """

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class ConfigurationError(UltraZException):
    """
    Raised when application configuration is invalid.
    """


class DatabaseError(UltraZException):
    """
    Raised when a database operation fails.
    """


class RuntimeError(UltraZException):
    """
    Raised when an AI runtime fails.
    """


class MemoryError(UltraZException):
    """
    Raised when a memory operation fails.
    """


class ToolError(UltraZException):
    """
    Raised when a tool execution fails.
    """


class AuthenticationError(UltraZException):
    """
    Raised when authentication fails.
    """


class AuthorizationError(UltraZException):
    """
    Raised when authorization fails.
    """


class ValidationError(UltraZException):
    """
    Raised when validation fails.
    """