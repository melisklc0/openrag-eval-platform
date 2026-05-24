from fastapi import FastAPI

from openrag_eval.api.exception_handlers import register_exception_handlers
from openrag_eval.api.router import api_router
from openrag_eval.core.config import get_settings
from openrag_eval.observability.logger import setup_logging


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    settings = get_settings()
    setup_logging()

    app = FastAPI(
        title=settings.project_name,
        version=settings.version,
    )
    register_exception_handlers(app)
    app.include_router(api_router)
    return app


app = create_app()
