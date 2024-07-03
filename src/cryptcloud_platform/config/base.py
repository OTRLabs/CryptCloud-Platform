



@lru_cache(maxsize=1, typed=True)
def get_settings() -> Settings:
    return Settings.from_env()



