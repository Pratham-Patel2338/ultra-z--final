"""
Dummy runtime used for testing.
"""

from app.core.logger import logger
from app.runtime.base import Runtime
from app.runtime.metadata import RuntimeMetadata

class DummyRuntime(Runtime):
    """
    Simple runtime for testing.
    """

    def __init__(self) -> None:
    
        super().__init__(
            RuntimeMetadata(
                name="dummy",
                description="Dummy Runtime",
            )
        )

    async def start(self) -> None:
        logger.info("Dummy Runtime Started")

    async def stop(self) -> None:
        logger.info("Dummy Runtime Stopped")