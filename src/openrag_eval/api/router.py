from fastapi import APIRouter

from openrag_eval.api.routers import health


api_router = APIRouter()
api_router.include_router(health.router)
