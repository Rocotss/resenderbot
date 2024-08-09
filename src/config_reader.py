from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    API_ID: int
    API_HASH: str
    GROUP_ID: int
    ADMIN_ID: int

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


config = Settings()
