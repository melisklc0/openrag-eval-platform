from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class DocumentMetadata(BaseModel):
    source: str | None = None
    source_url: str | None = None
    language: str = "en"
    tags: list[str] = Field(default_factory=list)


class DocumentCreate(BaseModel):
    title: str
    content: str
    metadata: DocumentMetadata = Field(default_factory=DocumentMetadata)


class DocumentRead(BaseModel):
    id: UUID
    title: str
    content: str
    metadata: DocumentMetadata
    created_at: datetime


class DocumentUpdate(BaseModel):
    title: str | None = None
    content: str | None = None
    metadata: DocumentMetadata | None = None
