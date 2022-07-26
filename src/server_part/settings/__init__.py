"""Declare way to get settings."""
from settings import base, prod, test, dev

from enum import Enum


class SettingsVariations(Enum):
    """Declare variations of app settings."""

    prod: str = 'prod'
    dev: str = 'dev'
    test: str = 'test'


NAME_DISTRO: dict[SettingsVariations, type[base.Base]] = {
    SettingsVariations.prod: prod.ProductionSettings,
    SettingsVariations.dev: dev.DevelopmentSettings,
    SettingsVariations.test: test.TestSettings,
}


class Settings:
    """Main class for interaction with settings."""

    declared_env: SettingsVariations = SettingsVariations.prod
    is_modified: bool = False

    @classmethod
    def declare_env(cls, env: SettingsVariations) -> None:
        """Set up `declared_env` variable."""
        if cls.is_modified:
            raise RuntimeError(
                'Can not declare settings twice during running.')
        cls.declared_env = env
        cls.is_modified = True

    @classmethod
    def get_settings(cls) -> base.Base:
        """Return choisen type of settings."""
        return NAME_DISTRO[cls.declared_env]()
