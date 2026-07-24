"""
Central Event Bus for ULTRA-Z.
"""

from __future__ import annotations

from app.core.logger import logger
from app.events.dispatcher import EventDispatcher
from app.events.event import Event
from app.events.registry import EventRegistry


class EventBus:
    """
    Publish/Subscribe event bus.
    """

    def __init__(self) -> None:
        self._registry = EventRegistry()
        self._dispatcher = EventDispatcher()

    def subscribe(
        self,
        event_name: str,
        handler,
    ) -> None:
        """
        Register an event handler.
        """

        logger.info(f"Subscribed handler to '{event_name}'")

        self._registry.subscribe(
            event_name,
            handler,
        )

    async def publish(
        self,
        event: Event,
    ) -> None:
        """
        Publish an event.
        """

        logger.debug(
            "Publishing event "
            f"{event.name} "
            f"(priority={event.priority.name}, "
            f"source={event.source})"
        )

        handlers = self._registry.get_handlers(
            event.name,
        )

        await self._dispatcher.dispatch(
            event,
            handlers,
        )


event_bus = EventBus()