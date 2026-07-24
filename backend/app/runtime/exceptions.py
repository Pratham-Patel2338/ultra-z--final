"""
Runtime exceptions.
"""


class RuntimeError(Exception):
    """
    Base runtime exception.
    """


class RuntimeConfigurationError(RuntimeError):
    """
    Invalid runtime configuration.
    """


class RuntimeDependencyError(RuntimeError):
    """
    Invalid runtime dependency graph.
    """


class RuntimeStartupError(RuntimeError):
    """
    Runtime failed to start.
    """


class RuntimeShutdownError(RuntimeError):
    """
    Runtime failed to stop.
    """


class RuntimeHealthError(RuntimeError):
    """
    Runtime health check failed.
    """