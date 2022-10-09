import json
from functools import lru_cache
from typing import Any, Dict, List

from .config import settings


@lru_cache(maxsize=settings.FIXTURES_LOAD_MAX)
def load_fixture(
    path: str, sorting_field: str | None = None, reverse: bool = False
) -> List[Dict[str, Any]]:
    f = open(settings.FIXTURES_DIR / path)
    data = json.load(f)
    f.close()

    if sorting_field:
        data = sorted(data, key=lambda v: v[sorting_field], reverse=reverse)

    return data
