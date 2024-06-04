from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8'
    )

    postgres_db: str
    postgres_user: str
    postgres_password: str
    postgres_port: str
    postgres_host: str

    secret_key: str
    algorithm: str

    mail_username: str
    mail_password: str
    mail_from: str
    mail_port: int
    mail_server: str
    mail_validate_cert: bool

    origins: list[str]

    cloudinary_name: str
    cloudinary_api_key: str
    cloudinary_api_secret: str

    def postgres_url(self) -> str:
        return f"postgresql://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}"


settings = Settings()
