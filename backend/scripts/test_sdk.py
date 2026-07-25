# scripts/test_sdk.py

import asyncio
from ollama import AsyncClient

async def main():
    client = AsyncClient(host="http://localhost:11434")

    response = await client.chat(
        model="qwen3:8b",
        messages=[
            {
                "role": "user",
                "content": "Hello"
            }
        ]
    )

    print(response.message.content)

asyncio.run(main())