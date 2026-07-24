"""
System events used by ULTRA-Z.
"""

from app.events.event import Event


class ApplicationStartedEvent(Event):
    """
    Fired when the application has finished starting.
    """

    def __init__(self) -> None:
        super().__init__(
            name="application.started",
            source="system",
        )


class ApplicationStoppedEvent(Event):
    """
    Fired when the application is shutting down.
    """

    def __init__(self) -> None:
        super().__init__(
            name="application.stopped",
            source="system",
        )