"""
Application lifecycle management.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.logger import logger
from app.core.settings import settings

from app.database.manager import database_manager

from app.events.event_bus import event_bus
from app.events.system_events import (
    ApplicationStartedEvent,
    ApplicationStoppedEvent,
)

from app.events.system_handlers import (
    log_application_started,
    log_application_stopped,
)

from app.runtime.dummy_runtime import DummyRuntime
from app.runtime.manager import runtime_manager



@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Manage application startup and shutdown.
    """

    logger.info("=" * 60)
    logger.info("Starting ULTRA-Z")
    logger.info(f"Version : {settings.app_version}")
    logger.info("=" * 60)
    await database_manager.initialize()
    await event_bus.publish(
        ApplicationStartedEvent()
    )
    runtime_manager.register(
        DummyRuntime()
    )

    await runtime_manager.start_all()
    # Future startup sequence
    #
    # Database
    # Event Bus
    # Runtime
    # Memory
    # Assistant

    yield
    await event_bus.publish(
        ApplicationStoppedEvent()
    )
    await runtime_manager.stop_all()
    await database_manager.shutdown()
    logger.info("=" * 60)
    logger.info("Stopping ULTRA-Z")
    logger.info("=" * 60)
    
    
event_bus.subscribe(
    "application.started",
    log_application_started,
)

event_bus.subscribe(
    "application.stopped",
    log_application_stopped,
)