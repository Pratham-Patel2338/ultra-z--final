from app.assistant.manager import ConversationManager

import pytest

from app.assistant.exceptions import ConversationNotFoundError

def test_invalid_conversation():
    manager = ConversationManager()

    with pytest.raises(ConversationNotFoundError):
        manager.get("invalid-id")


def test_create_conversation():
    manager = ConversationManager()

    conversation = manager.create()

    assert conversation is not None
    assert manager.count() == 1


def test_exists():
    manager = ConversationManager()

    conversation_id = manager.create()

    assert manager.exists(conversation_id)

def test_get():
    manager = ConversationManager()

    conversation_id = manager.create()

    conversation = manager.get(conversation_id)

    assert conversation is not None

def test_delete():
    manager = ConversationManager()

    conversation_id = manager.create()

    manager.delete(conversation_id)

    assert manager.count() == 0


def test_list_ids():
    manager = ConversationManager()

    id1 = manager.create()
    id2 = manager.create()

    ids = manager.list_ids()

    assert id1 in ids
    assert id2 in ids