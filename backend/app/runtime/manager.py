"""
Runtime manager for ULTRA-Z.
"""

from __future__ import annotations

from app.core.logger import logger
from app.runtime.base import Runtime
from app.runtime.registry import RuntimeRegistry
from app.runtime.state import RuntimeState
from app.runtime.dependency import DependencyResolver

class RuntimeManager:
    """
    Manages all runtime services.
    """
    @property
    def registry(self) -> RuntimeRegistry:
        """
        Expose runtime registry.
        """
        return self._registry

    def __init__(self) -> None:
        self._registry = RuntimeRegistry()
        
        self._resolver = DependencyResolver()

    def register(self, runtime: Runtime) -> None:
        """
        Register a runtime.
        """
        logger.info(f"Registering runtime: {runtime.name}")
        self._registry.register(runtime)

    async def start_all(self) -> None:
        """
        Start all registered runtimes.
        """
        ordered = self._resolver.resolve(
            self._registry.all()
        )

        for runtime in ordered:
            logger.info(f"Starting runtime: {runtime.name}")

            runtime.state = RuntimeState.STARTING

            try:
                await runtime.start()

                runtime.state = RuntimeState.RUNNING

                logger.info(f"Runtime started: {runtime.name}")

            except Exception:
                runtime.state = RuntimeState.ERROR

                logger.exception(
                    f"Failed to start runtime: {runtime.name}"
                )

    async def stop_all(self) -> None:
        """
        Stop all registered runtimes.
        """
        ordered = self._resolver.resolve(
            self._registry.all()
        )

        for runtime in reversed(ordered):
            logger.info(f"Stopping runtime: {runtime.name}")

            runtime.state = RuntimeState.STOPPING

            try:
                await runtime.stop()

                runtime.state = RuntimeState.STOPPED

                logger.info(f"Runtime stopped: {runtime.name}")

            except Exception:
                runtime.state = RuntimeState.ERROR

                logger.exception(
                    f"Failed to stop runtime: {runtime.name}"
                )


runtime_manager = RuntimeManager()