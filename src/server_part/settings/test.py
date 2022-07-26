"""Test settings."""
from settings.base import Base

from pydantic import SecretStr


class TestSettings(Base):
    """Declare prod settings."""

    debug: bool = True
    title: str = "Testing Airhocke"

    secret_key: SecretStr = SecretStr("test_secret")

    max_connection_count: int = 5
    min_connection_count: int = 5
