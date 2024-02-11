from pydantic import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')

    # Application settings
    APP_NAME: str = "FastAPI"

    # Database settings
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    DB_URI: str



settings = Settings()