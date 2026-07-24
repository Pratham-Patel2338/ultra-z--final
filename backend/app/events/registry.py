"""
Event registry.
"""

from collections import defaultdict
from collections.abc import Awaitable, Callable

from app.events.event import Event

EventHandler = Callable[[Event], Awaitable[None]]


class EventRegistry:
    """
    Stores all event subscriptions.
    """

    def __init__(self) -> None:
        self._handlers: dict[str, list[EventHandler]] = defaultdict(list)

    def subscribe(
        self,
        event_name: str,
        handler: EventHandler,
    ) -> None:
        """
        Register an async event handler.
        """

        if handler in self._handlers[event_name]:
            return

        self._handlers[event_name].append(handler)

    def get_handlers(
        self,
        event_name: str,
    ) -> list[EventHandler]:
        """
        Return handlers for an event.
        """

        return self._handlers.get(event_name, [])