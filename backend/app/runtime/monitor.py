"""
Runtime monitor.
"""

from __future__ import annotations

import asyncio

from app.core.logger import logger
from app.runtime.manager import RuntimeManager


class RuntimeMonitor:
    """
    Periodically checks runtime health.
    """

    def __init__(
        self,
        manager: RuntimeManager,
        interval: int = 10,
    ) -> None:
        self._manager = manager
        self._interval = interval
        self._running = False

    async def start(self) -> None:
        """
        Start monitoring.
        """

        self._running = True

        logger.info("Runtime Monitor Started")

        while self._running:

            await self.check_all()

            await asyncio.sleep(self._interval)

    async def stop(self) -> None:
        """
        Stop monitoring.
        """

        self._running = False

        logger.info("Runtime Monitor Stopped")

    async def check_all(self) -> None:
        """
        Check health of every runtime.
        """

        for runtime in self._manager.registry.all():

            health = await runtime.health_check()

            logger.info(
                f"[{health.name}] "
                f"healthy={health.healthy} "
                f"state={health.state.value}"
            )