from fastapi import APIRouter

from openrag_eval.api.routers import document, health


api_router = APIRouter()
api_router.include_router(health.router)
api_router.include_router(document.router)
