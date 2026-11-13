"""Cryptographically secure password generation."""

import secrets
import string

LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
DIGITS = string.digits
SYMBOLS = "!@#$%^&*()-_=+[]{}?"

CHARACTER_POOL = LOWERCASE + UPPERCASE + DIGITS + SYMBOLS

MIN_LENGTH = 20
MAX_LENGTH = 128


def validate_length(length: int) -> None:
    """Raise if ``length`` is not an int within the supported range."""
    if not isinstance(length, int) or isinstance(length, bool):
        raise TypeError("Password length must be an integer.")
    if not MIN_LENGTH <= length <= MAX_LENGTH:
        raise ValueError(
            f"Password length must be between {MIN_LENGTH} and {MAX_LENGTH}."
        )


def generate_password(length: int = 32) -> str:
    """
    Generate a cryptographically secure random password.

    Guarantees at least one lowercase, uppercase, digit and symbol.
    Uses only the ``secrets`` module (OS-backed CSPRNG).
    """
    validate_length(length)

    password = [
        secrets.choice(LOWERCASE),
        secrets.choice(UPPERCASE),
        secrets.choice(DIGITS),
        secrets.choice(SYMBOLS),
    ]
    password.extend(secrets.choice(CHARACTER_POOL) for _ in range(length - 4))

    # Shuffle so the guaranteed characters are not in predictable positions.
    secrets.SystemRandom().shuffle(password)
    return "".join(password)
