from typing import Any, Dict, Optional

from pydantic import BaseModel


class User(BaseModel):
    id: Optional[int]
    first_name: str
    last_name: str
    full_name: str

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]):
        return cls(
            id=obj["id"],
            first_name=obj["first_name"],
            last_name=obj["last_name"],
            full_name=f'{obj["first_name"]} {obj["last_name"]}',
        )


class CreateUser(BaseModel):
    first_name: str
    last_name: str
