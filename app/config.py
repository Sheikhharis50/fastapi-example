from pathlib import Path


class AppSettings:
    FIXTURES_DIR = Path("app", "fixtures")
    FIXTURES_LOAD_MAX = 10


settings = AppSettings()
