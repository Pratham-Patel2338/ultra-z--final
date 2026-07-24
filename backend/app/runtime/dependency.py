"""
Runtime dependency resolver.
"""

from __future__ import annotations

from app.runtime.base import Runtime
from app.runtime.exceptions import RuntimeDependencyError


class DependencyResolver:
    """
    Resolves runtime startup order.
    """

    def resolve(
        self,
        runtimes: list[Runtime],
    ) -> list[Runtime]:

        resolved: list[Runtime] = []

        visited: set[str] = set()

        visiting: set[str] = set()

        runtime_map = {
            runtime.name: runtime
            for runtime in runtimes
        }

        def visit(runtime: Runtime) -> None:

            if runtime.name in visited:
                return

            if runtime.name in visiting:
                raise RuntimeDependencyError(
                    f"Circular dependency detected involving '{runtime.name}'."
                )

            visiting.add(runtime.name)

            for dependency in runtime.metadata.dependencies:

                if dependency not in runtime_map:
                    raise RuntimeDependencyError(
                        f"Runtime '{runtime.name}' depends on "
                        f"'{dependency}', but it is not registered."
                    )

                visit(runtime_map[dependency])

            visiting.remove(runtime.name)

            visited.add(runtime.name)

            resolved.append(runtime)

        for runtime in runtimes:
            visit(runtime)

        return resolved