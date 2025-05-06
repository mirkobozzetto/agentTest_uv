from collections.abc import Iterator
from .client import stream_chat
from .history import InMemoryHistory
from .cost import dollars
from .config import settings

_history = InMemoryHistory(max_messages=20)

def chat_stream(user_prompt: str) -> Iterator[str]:
    """Token-by-token stream and memory update."""
    _history.add("user", user_prompt)
    messages = _history.context()

    for token in stream_chat(messages):
        yield token                      # streaming direct

    # OpenAI returns `usage` on the **last** chunk → not available here
    # ⇒ cost calculated by client or via a future hook

def chat_once(user_prompt: str) -> str:
    """Complete response in one go."""
    return "".join(chat_stream(user_prompt))

def cost_estimate(total_tokens: int) -> float:
    return dollars(settings.model, total_tokens)
