"""Declare base for fastapi settings."""
from enum import Enum

from pydantic import BaseSettings, Field


class EnvTypes(Enum):
    """Declare possible environment types for app."""

    prod: str = 'prod'
    dev: str = 'dev'
    test: str = 'test'


class BaseAppSettings(BaseSettings):
    """Base for app settings."""

    app_env: EnvTypes = EnvTypes.prod

    class Config:
        """Base app settings class configuration."""

        env_file = '.env'
        env_file_encoding = 'utf-8'
