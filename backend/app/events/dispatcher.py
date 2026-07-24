"""
Event dispatcher.

Responsible for safely executing all handlers for an event.
"""

from __future__ import annotations

import asyncio

from app.core.logger import logger
from app.events.event import Event
from app.events.registry import EventHandler


class EventDispatcher:
    """
    Dispatches events to all registered handlers.
    """

    async def dispatch(
        self,
        event: Event,
        handlers: list[EventHandler],
    ) -> None:
        """
        Dispatch an event to every subscribed handler.

        One failing handler should never stop the others.
        """

        if not handlers:
            logger.debug(f"No handlers registered for event: {event.name}")
            return

        tasks = [
            self._safe_execute(handler, event)
            for handler in handlers
        ]

        await asyncio.gather(*tasks)

    async def _safe_execute(
        self,
        handler: EventHandler,
        event: Event,
    ) -> None:
        """
        Execute a single handler safely.
        """

        try:
            await handler(event)

        except Exception:
            logger.exception(
                f"Event handler failed while processing '{event.name}'"
            )