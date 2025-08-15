import os.path
import pathlib
import string

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

BASEDIR = pathlib.Path(__file__).parent


class Uvicorn(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8000
    reload: bool = True


class ApiV1(BaseModel):
    prefix: str = "/v1"


class Link(BaseModel):
    chars: str = string.digits + string.ascii_letters
    length: int = 6


class Database(BaseModel):
    url: str
    echo: bool = True
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=os.path.join(BASEDIR.as_posix(), "../.env"),
        extra="allow",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
    )
    api_v1: ApiV1 = ApiV1()
    link: Link = Link()
    uvicorn: Uvicorn = Uvicorn()
    db: Database


settings = Settings()  # noqa can be added to cache
