from collections.abc import Iterator
from .client import stream_chat
from .history import InMemoryHistory
from .config import settings

_history = InMemoryHistory(max_messages=20)

def chat_stream(user_prompt: str) -> Iterator[str]:
    """Token-by-token stream and memory update."""
    _history.add("user", user_prompt)
    messages = _history.context()

    response_content = ""
    for token in stream_chat(messages):
        response_content += token
        yield token

    _history.add("assistant", response_content)

def chat_once(user_prompt: str) -> str:
    """Complete response in one go."""
    return "".join(chat_stream(user_prompt))
