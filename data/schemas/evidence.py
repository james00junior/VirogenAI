"""Scientific evidence record schema."""

from datetime import date

from pydantic import BaseModel, Field


class EvidenceRecord(BaseModel):
    """Normalized metadata for a scientific evidence item."""

    evidence_id: str = Field(min_length=1)
    title: str = Field(min_length=1)
    source_type: str = Field(min_length=1)
    source_url: str | None = None
    authors: list[str] = Field(default_factory=list)
    publication_date: date | None = None
    doi: str | None = None
    abstract: str | None = None
    tags: list[str] = Field(default_factory=list)
