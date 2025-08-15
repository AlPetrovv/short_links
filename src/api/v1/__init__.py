from fastapi import APIRouter

from config import settings
from .links import router as links_router

api_v1_router = APIRouter(prefix=settings.api_v1.prefix)

api_v1_router.include_router(links_router)

__all__ = ["api_v1_router"]