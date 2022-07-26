"""Declare parent of all settings classes."""
from pydantic import BaseSettings, SecretStr, PostgresDsn


class Base(BaseSettings):
    """Declare all basic settings."""

    # Project stuff
    debug: bool = False

    # Db stuff

    database_url: PostgresDsn
    max_connection_count: int = 10
    min_connection_count: int = 10

    # API stuff

    secret_key: SecretStr
    api_prefix: str = '/api/v1'
    allowed_hosts: list[str] = ['*']

    # Email related stuff

    email_host: str = 'smtp.gmail.com'
    email_host_user: str
    email_host_password: SecretStr

    class Config:
        """Configuration of the class."""

        env_file = '.env'
        env_file_encoding = 'utf-8'
        validate_assignment = True
