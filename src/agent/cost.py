# Simplified prices (USD / 1K tokens)
_PRICES = {
    "gpt-4o-mini": 0.0005,
}


def dollars(model: str, total_tokens: int) -> float:
    rate = _PRICES.get(model, 0.001)
    return round(total_tokens / 1000 * rate, 6)
