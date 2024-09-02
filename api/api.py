from fastapi import APIRouter

from api import query_api,location


api_router = APIRouter(prefix="/api")

api_router.include_router(query_api.router, prefix="/v1")
api_router.include_router(location.router, prefix="/v1")

