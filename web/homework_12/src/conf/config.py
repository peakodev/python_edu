from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8'
    )

    postgres_db: str = 'contacts'
    postgres_user: str = 'test'
    postgres_password: str = 'test'
    postgres_port: str = '5432'
    postgres_host: str = 'localhost'

    redis_host: str = 'localhost'
    redis_port: int = 6379

    redis_cache_time: int = 900

    secret_key: str = 'secret'
    algorithm: str = 'HS256'

    mail_username: str = 'username'
    mail_password: str = 'password'
    mail_from: str = 'test@example.com'
    mail_port: int = 587
    mail_server: str = 'smtp.example.com'
    mail_validate_cert: bool = True

    origins: list[str] = ['http://localhost', 'http://localhost:8080']

    cloudinary_name: str = 'name'
    cloudinary_api_key: str = 'key'
    cloudinary_api_secret: str = 'secret'

    def postgres_url(self) -> str:
        return f"postgresql://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}"


settings = Settings()
