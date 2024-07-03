from __future__ import annotations

import binascii
import json
import os
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import TYPE_CHECKING, Any, Final

from advanced_alchemy.utils.text import slugify
from litestar.serialization import decode_json, encode_json
from litestar.utils.module_loader import module_to_os_path
from redis.asyncio import Redis
from sqlalchemy import event
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlalchemy.pool import NullPool

if TYPE_CHECKING:
    from litestar.data_extractors import RequestExtractorField, ResponseExtractorField

DEFAULT_MODULE_NAME = "app"
BASE_DIR: Final[Path] = module_to_os_path(DEFAULT_MODULE_NAME)

TRUE_VALUES = {"True", "true", "1", "yes", "Y", "T"}






@dataclass
class Settings:
    app: AppSettings = field(default_factory=AppSettings)
    db: DatabaseSettings = field(default_factory=DatabaseSettings)
    vite: ViteSettings = field(default_factory=ViteSettings)
    server: ServerSettings = field(default_factory=ServerSettings)
    log: LogSettings = field(default_factory=LogSettings)
    redis: RedisSettings = field(default_factory=RedisSettings)
    saq: SaqSettings = field(default_factory=SaqSettings)

    @classmethod
    def from_env(cls, dotenv_filename: str = ".env") -> Settings:
        from litestar.cli._utils import console

        env_file = Path(f"{os.curdir}/{dotenv_filename}")
        if env_file.is_file():
            from dotenv import load_dotenv

            console.print(f"[yellow]Loading environment configuration from {dotenv_filename}[/]")

            load_dotenv(env_file)
        return Settings()


@lru_cache(maxsize=1, typed=True)
def get_settings() -> Settings:
    return Settings.from_env()