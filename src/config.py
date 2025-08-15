import os.path
import pathlib

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

BASEDIR = pathlib.Path(__file__).parent


class Uvicorn(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000
    reload: bool = True

class ApiV1(BaseModel):
    prefix: str = "/v1"


class Database(BaseModel):
    url: str
    echo: bool = True
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10
    naming_conversations = Field(
        default={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_N_name)s",
            "ck": "ck_%(table_name)s_%(constraint_name)s",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        }
    )


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=os.path.join(BASEDIR.as_posix(), "../.db_helper.pyenv"),
        extra="allow",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
    )
    api: ApiV1 = ApiV1()
    db: Database
    uvicorn: Uvicorn = Uvicorn()


settings = Settings()
