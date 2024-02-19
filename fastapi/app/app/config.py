from typing import Any, Optional, Dict, List

from pydantic import (
    PostgresDsn,
    validator,
)

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # model_config = SettingsConfigDict(env_file='.env')

    # Application settings
    APP_NAME: str = "FastAPI"

    # Database settings
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_SERVER: str
    POSTGRES_PORT: int = 5432
    POSTGRES_URI: Optional[PostgresDsn] = None
    
    # needs to be updated (deprecated)
    @validator("POSTGRES_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            username=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            port=values.get("POSTGRES_PORT"),
            path=values.get('POSTGRES_DB')
        )


settings = Settings()
