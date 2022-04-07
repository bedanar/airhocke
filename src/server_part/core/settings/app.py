"""Declare main class for app settings."""
import logging

from typing import Any
from core.settings.base import BaseAppSettings
from pydantic import PostgresDsn, SecretStr


class AppSettings(BaseAppSettings):
    """Set up app settings."""

    debug: bool = False
    docs_url: str = "/docs"
    openapi_prefix: str = ""
    openapi_url: str = "/openapi.json"
    redoc_url: str = "/redoc"
    title: str = "FastAPI example application"
    version: str = "0.0.0"

    database_url: PostgresDsn
    max_connection_count: int = 10
    min_connection_count: int = 10

    secret_key: SecretStr

    api_prefix: str = "/api"

    jwt_token_prefix: str = "Token"

    allowed_hosts: list[str] = ["*"]

    logging_level: int = logging.INFO
    loggers: tuple[str, str] = ("uvicorn.asgi", "uvicorn.access")

    class Config:
        validate_assignment = True

    @property
    def fastapi_kwargs(self) -> dict[str, Any]:
        return {
            "debug": self.debug,
            "docs_url": self.docs_url,
            "openapi_prefix": self.openapi_prefix,
            "openapi_url": self.openapi_url,
            "redoc_url": self.redoc_url,
            "title": self.title,
            "version": self.version,
        }
