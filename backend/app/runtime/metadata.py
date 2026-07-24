"""
Runtime metadata definitions.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class RuntimeMetadata:
    """
    Describes a runtime service.
    """

    name: str

    version: str = "1.0.0"

    description: str = ""

    author: str = "ULTRA-Z"

    dependencies: list[str] = field(default_factory=list)

    auto_start: bool = True

    critical: bool = False