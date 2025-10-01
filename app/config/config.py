from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent.parent


class RunConfig(BaseModel):
    host: str
    port: int


class ApiPrefix(BaseModel):
    temperatures: str = "/temperatures"


class WeatherApiSettings(BaseSettings):
    city: str = "Kyiv"
    url: str = "http://api.openweathermap.org/data/2.5/weather"
    api_key: str


class DatabaseConfig(BaseModel):
    url: str
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10


class RedisClient(BaseSettings):
    host: str
    port: int
    db: int = 0
    expires: int

    @property
    def celery_url_backend(self) -> str:
        return f"redis://{self.host}:{self.port}/{self.db}"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env.template",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
    )

    run: RunConfig
    api_prefix: ApiPrefix = ApiPrefix()
    weather_api: WeatherApiSettings
    db: DatabaseConfig
    redis: RedisClient


settings = Settings()
