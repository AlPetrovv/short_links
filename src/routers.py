from fastapi import APIRouter
from api.v1 import api_v1_router

# main_router
main_router = APIRouter(prefix="/api")

main_router.include_router(api_v1_router)
