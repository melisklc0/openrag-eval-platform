from fastapi import FastAPI


def register_exception_handlers(app: FastAPI) -> None:
    """Register HTTP exception handlers for application errors."""
