import asyncio

from app.services.llm.chat import chat_service


async def main():

    response = await chat_service.generate(
        prompt="Hello! Introduce yourself in one sentence."
    )

    print()
    print("=" * 60)
    print("ULTRA-Z FIRST RESPONSE")
    print("=" * 60)
    print(response.text)
    print("=" * 60)
    print()
    print("Model:", response.model)


asyncio.run(main())