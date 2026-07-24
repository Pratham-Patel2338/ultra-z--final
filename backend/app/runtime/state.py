"""
Runtime states.
"""

from enum import Enum


class RuntimeState(Enum):
    """
    Lifecycle state of a runtime.
    """

    CREATED = "created"
    STARTING = "starting"
    RUNNING = "running"
    STOPPING = "stopping"
    STOPPED = "stopped"
    ERROR = "error"