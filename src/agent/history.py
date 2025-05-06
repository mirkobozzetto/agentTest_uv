from collections.abc import Iterator


class InMemoryHistory:
    """Simple memory: keep N messages."""

    def __init__(self, max_messages: int = 20):
        self._messages: list[dict] = []
        self._max = max_messages

    def add(self, role: str, content: str) -> None:
        self._messages.append({"role": role, "content": content})
        if len(self._messages) > self._max:
            self._messages.pop(0)

    def context(self) -> list[dict]:
        return self._messages.copy()

    def __iter__(self) -> Iterator[dict]:
        return iter(self._messages)
