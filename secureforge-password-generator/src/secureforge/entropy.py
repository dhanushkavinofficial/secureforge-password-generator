"""Password entropy estimation."""

import math

from .generator import (
    CHARACTER_POOL,
    DIGITS,
    LOWERCASE,
    SYMBOLS,
    UPPERCASE,
    validate_length,
)


def estimate_entropy(length: int) -> float:
    """Estimate entropy (bits) of the independent random character choices.

    This is a conservative model: it ignores the extra entropy from the
    final shuffle and is not a formal proof of output-space size.
    """
    validate_length(length)

    mandatory = sum(
        math.log2(len(group)) for group in (LOWERCASE, UPPERCASE, DIGITS, SYMBOLS)
    )
    remaining = (length - 4) * math.log2(len(CHARACTER_POOL))
    return mandatory + remaining


def rate_strength(bits: float) -> str:
    """Map an entropy estimate to a human-readable rating."""
    if bits < 80:
        return "Weak"
    if bits < 128:
        return "Strong"
    return "Very strong"
