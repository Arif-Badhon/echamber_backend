from pydantic import AnyHttpUrl, BaseSettings, HttpUrl, validator
from typing import Union, List, Optional
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    API_V2_STR: str = "/api/v2"
    DATABASE_URL: str = os.environ.get("DATABASE_URL")
    SECRET_KEY: str = os.environ.get("SECRET_KEY")
    ALGORITHM: str = os.environ.get("ALGORITHM")
    SMS_USERNAME: str = os.environ.get("SMS_USERNAME")
    SMS_PASSWORD: str = os.environ.get("SMS_PASSWORD")
    SMS_FROM: str = os.environ.get("SMS_FROM")

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        os.environ.get("URL_ONE"),
        os.environ.get("URL_TWO"),
    ]

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    PROJECT_NAME: str = "E-Chamber"
    SENTRY_DSN: Optional[HttpUrl] = None

    class Config:
        case_sensitive = True


settings = Settings()
