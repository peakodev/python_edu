from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8'
    )

    postgres_url: str
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


settings = Settings()
