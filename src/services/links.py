import secrets

from config import settings


def create_code() -> str:
    """Create random string of length {settings.link.length}"""
    code = "".join(
        secrets.choice(settings.link.chars) for _ in range(settings.link.length)
    )
    return code
