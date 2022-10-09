from typing import Any, Dict, List

from fastapi import HTTPException

from app.dependencies import load_fixture
from app.utils import is_subdict

from .models import CreateUser, User

users_db: List[Dict[str, Any]] = load_fixture("users.json", "id")


async def is_exist(records_list: List[Dict[str, Any]], new_record: Dict[str, Any]):
    return len(list(filter(lambda r: is_subdict(r, new_record), records_list))) > 0


async def next_id(data: List[Dict[str, Any]]) -> int:
    return data[-1]["id"] + 1 if len(data) else 1


async def users() -> List[User]:
    return list(map(User.from_dict, users_db))


async def create_user(user: CreateUser) -> User:
    if await is_exist(users_db, user.dict()):
        raise HTTPException(status_code=400, detail="User already exists.")

    return User.from_dict({**user.dict(), "id": await next_id(users_db)})
