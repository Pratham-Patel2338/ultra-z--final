"""
Application lifecycle management.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.logger import logger
from app.core.settings import settings

from app.database.manager import database_manager


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
    # Future startup sequence
    #
    # Database
    # Event Bus
    # Runtime
    # Memory
    # Assistant

    yield
    await database_manager.shutdown()
    logger.info("=" * 60)
    logger.info("Stopping ULTRA-Z")
    logger.info("=" * 60)