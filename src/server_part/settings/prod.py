"""Production settings."""
from settings.base import Base


class ProductionSettings(Base):
    """Declare prod settings."""

    title: str = "Airhocke"

    class Config(Base.Config):
        """Configure production properties of the project."""

        env_file = '.env.prod'
