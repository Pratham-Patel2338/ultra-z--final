"""
Simple dependency container.

This will evolve into the central dependency registry
for ULTRA-Z.
"""

from __future__ import annotations


class DependencyContainer:
    """
    Stores shared application services.
    """

    def __init__(self):
        self._services: dict[str, object] = {}

    def register(self, name: str, service: object) -> None:
        """
        Register a service.
        """
        self._services[name] = service

    def get(self, name: str) -> object:
        """
        Retrieve a registered service.
        """
        return self._services[name]


container = DependencyContainer()