"""
ULTRA-Z Backend Entry Point.
"""

from fastapi import FastAPI

from app.core.lifecycle import lifespan
from app.core.settings import settings

from app.database.manager import database_manager

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug,
    lifespan=lifespan,
)


@app.get("/")
async def root():
    return {
        "status": "online",
        "assistant": settings.app_name,
        "version": settings.app_version,
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
    }
    

@app.get("/health/database")
async def database_health():
    """
    Database health check.
    """

    healthy = await database_manager.health_check()

    return {
        "database": "healthy" if healthy else "unhealthy"
    }