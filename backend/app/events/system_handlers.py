"""
System event handlers.
"""

from app.core.logger import logger
from app.events.event import Event


async def log_application_started(event: Event) -> None:
    logger.info("Application Started Event Received")


async def log_application_stopped(event: Event) -> None:
    logger.info("Application Stopped Event Received")