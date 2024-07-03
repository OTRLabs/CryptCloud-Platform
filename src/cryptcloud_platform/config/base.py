from __future__ import annotations
from functools import lru_cache
import binascii
import json
from pathlib import Path
from dataclasses import dataclass, field
import os
from typing import TYPE_CHECKING, Any, Final

@dataclass
class Settings:
    
    print("Loading settings")
    ## pull in CryptCloud component settings
    # app: AppSettings = field(default_factory=AppSettings)
    # database: DatabaseSettings = field(default_factory=DatabaseSettings)
    # vite: ViteSettings = field(default_factory=ViteSettings)
    # server: ServerSettings = field(default_factory=ServerSettings)
    # saq: SAQSettings = field(default_factory=SAQSettings)
    # log: LoggingSettings = field(default_factory=LoggingSettings)
    
    
    @classmethod
    def from_env(cls, dotenv_filename: str = ".env") -> Settings:
        
        env_file = Path(f"{os.curdir}/{dotenv_filename}")

        if env_file.is_file():
            from dotenv import load_dotenv
            
            print(f"Loading environment variables from {env_file}")

            load_dotenv(env_file)

        return Settings()

@lru_cache(maxsize=1, typed=True)
def get_settings() -> Settings:
    return Settings.from_env()



