class ApplicationError(Exception):
    """Base exception for OpenRAG Eval application errors."""

    code = "application_error"
    status_code = 500

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)


class DocumentNotFoundError(ApplicationError):
    """Raised when a requested document does not exist."""

    code = "document_not_found"
    status_code = 404

    def __init__(self) -> None:
        super().__init__("Document not found")
