import asyncio

from app.assistant.manager import conversation_manager


async def main():

    conversation1 = conversation_manager.create(
        system_prompt="You are ULTRA-Z."
    )

    conversation2 = conversation_manager.create(
        system_prompt="You are ULTRA-Z."
    )

    chat1 = conversation_manager.get(conversation1)
    chat2 = conversation_manager.get(conversation2)

    print("=" * 60)
    print("Conversation IDs")
    print("=" * 60)

    print(conversation1)
    print(conversation2)

    print()

    await chat1.ask("My name is Pratham.")
    await chat2.ask("My name is Rahul.")

    response = await chat1.ask("What is my name?")
    print("Conversation 1:", response.text)

    response = await chat2.ask("What is my name?")
    print("Conversation 2:", response.text)

    print()
    print("=" * 60)
    print("Manager Statistics")
    print("=" * 60)

    print("Active Conversations:", conversation_manager.count())
    print("Conversation IDs:", conversation_manager.list_ids())


asyncio.run(main())

from app.assistant.exceptions import ConversationNotFoundError

try:
    conversation_manager.get("invalid-id")
except ConversationNotFoundError as e:
    print()
    print("=" * 60)
    print("Exception Test")
    print("=" * 60)
    print(e)