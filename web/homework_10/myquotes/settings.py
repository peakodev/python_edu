from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8'
    )

    postgres_db: str
    postgres_user: str
    postgres_pass: str
    postgres_port: str
    postgres_host: str

    mongo_user: str
    mongo_pass: str
    mongo_db_name: str
    mongo_domain: str


settings = Settings()
