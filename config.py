from pydantic import BaseModel, HttpUrl, FilePath
from pydantic_settings import BaseSettings, SettingsConfigDict


class TestDataConfig(BaseModel):
    image_png_file: FilePath
    response_limit: int
    search_radius: int


class HTTTPClientConfig(BaseModel):
    url: HttpUrl
    timeout: float

    @property
    def client_url(self) -> str:
        return str(self.url)


class LoggerConfig(BaseModel):
    path: str
    format: str
    rotation: str
    retention: int


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        extra="allow",
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="."
    )

    http_client: HTTTPClientConfig
    logger: LoggerConfig
    test_data: TestDataConfig


settings = Settings()
