"""
Database lifecycle manager.
"""

from sqlalchemy import text

from app.core.logger import logger

from .base import Base
from .session import engine


class DatabaseManager:
    """
    Handles database startup and health checks.
    """

    async def initialize(self) -> None:
        """
        Create database tables.
        """

        logger.info("Initializing database...")

        async with engine.begin() as connection:
            await connection.run_sync(Base.metadata.create_all)

        logger.info("Database initialized successfully.")

    async def shutdown(self) -> None:
        """
        Close database engine.
        """

        logger.info("Closing database...")

        await engine.dispose()

        logger.info("Database closed.")

    async def health_check(self) -> bool:
        """
        Verify database connectivity.
        """

        try:
            async with engine.connect() as connection:
                await connection.execute(text("SELECT 1"))

            return True

        except Exception:
            return False


database_manager = DatabaseManager()