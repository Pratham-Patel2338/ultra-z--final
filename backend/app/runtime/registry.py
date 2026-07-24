"""
Runtime registry.
"""

from app.runtime.base import Runtime


class RuntimeRegistry:
    """
    Stores all registered runtimes.
    """

    def __init__(self) -> None:
        self._runtimes: dict[str, Runtime] = {}

    def register(self, runtime: Runtime) -> None:
        """
        Register a runtime.
        """

        self._runtimes[runtime.name] = runtime

    def get(self, name: str) -> Runtime | None:
        """
        Get a runtime by name.
        """

        return self._runtimes.get(name)

    def all(self) -> list[Runtime]:
        """
        Return all runtimes.
        """

        return list(self._runtimes.values())