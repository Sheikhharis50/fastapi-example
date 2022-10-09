from fastapi import APIRouter

from .views import create_user, users

router = APIRouter(prefix="/account", tags=["account"])

# API routes
router.add_api_route(path="/user", endpoint=users, methods=["GET"])
router.add_api_route(path="/user/create", endpoint=create_user, methods=["POST"])
