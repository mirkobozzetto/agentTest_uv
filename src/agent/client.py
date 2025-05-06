"""
Isolated OpenAI client: SRP = talk to the API
Allows mocking in tests (depends on reversal in chat.py)
"""

from collections.abc import Iterator
import openai
from .config import settings

_openai_client = openai.OpenAI(api_key=settings.openai_api_key.get_secret_value())


def stream_chat(messages: list[dict]) -> Iterator[str]:
    """
    Send a prompt + context, return tokens as they are generated.
    """
    response = _openai_client.chat.completions.create(
        model=settings.model,
        messages=messages,
        temperature=settings.temperature,
        stream=True,
    )
    for chunk in response:
        delta = chunk.choices[0].delta
        if delta.content:
            yield delta.content


def last_usage_cost(response) -> tuple[int, int, int]:
    """Return (prompt_tokens, completion_tokens, total_tokens)."""
    usage = response.usage  # available on the last chunk
    return usage.prompt_tokens, usage.completion_tokens, usage.total_tokens
