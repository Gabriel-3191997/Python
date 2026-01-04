import secrets
import string
from typing import Optional


def generate_password(length: int = 8, use_punctuation: bool = True) -> str:
    """Generate a random password using cryptographically secure randomness.

    Args:
        length: Number of characters in the password (must be > 0).
        use_punctuation: Whether to include punctuation characters.

    Returns:
        A random password string.
    """
    if length <= 0:
        raise ValueError("length must be a positive integer")

    alphabet = string.ascii_letters + string.digits
    if use_punctuation:
        alphabet += string.punctuation

    return ''.join(secrets.choice(alphabet) for _ in range(length))


if __name__ == '__main__':
    print("Password:", generate_password(8))