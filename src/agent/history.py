from collections.abc import Iterator
from typing import List, Literal
from .client import ChatMessage


class InMemoryHistory:
    """Simple memory: keep N messages."""

    def __init__(self, max_messages: int = 20):
        self._messages: List[ChatMessage] = []
        self._max = max_messages

    def add(self, role: Literal["user", "assistant", "system"], content: str) -> None:
        message: ChatMessage = {"role": role, "content": content}
        self._messages.append(message)
        if len(self._messages) > self._max:
            self._messages.pop(0)

    def context(self) -> List[ChatMessage]:
        return self._messages.copy()

    def __iter__(self) -> Iterator[ChatMessage]:
        return iter(self._messages)
