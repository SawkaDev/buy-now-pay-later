from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    SERVER_PORT: int = 50051
    DB_HOST: str = "localhost"  # Default to localhost
    DB_PORT: int = 5432
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "postgres"
    DB_NAME: str = "api_key_service_db"

    @property
    def DATABASE_URL(self):
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
