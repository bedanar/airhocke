"""Declare dev settings."""
from settings.base import Base


class DevelopmentSettings(Base):
    """Declare dev settings."""

    debug: bool = True
    title: str = "Test airhocke"
