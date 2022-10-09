from fastapi import APIRouter

from .account import router as account_router

router = APIRouter(prefix="/v1")

router.include_router(router=account_router)
