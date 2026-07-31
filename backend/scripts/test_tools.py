import asyncio

from app.tools.context import ToolContext
from app.tools.dummy import DummyTool
from app.tools.executor import tool_executor
from app.tools.manager import tool_manager


async def main():

    tool_manager.clear()

    tool_manager.register(
        DummyTool(),
    )

    context = ToolContext(
        arguments={
            "name": "Pratham",
        }
    )

    result = await tool_executor.execute(
        "dummy",
        context,
    )

    print()

    print("=" * 60)
    print("ULTRA-Z TOOL TEST")
    print("=" * 60)

    print(result.success)
    print(result.message)

    print("=" * 60)


asyncio.run(main())