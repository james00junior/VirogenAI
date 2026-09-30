"""Provenance contracts required for explainable DRUGART predictions."""
from pydantic import BaseModel, Field


class PredictionProvenance(BaseModel):
    model_name: str = Field(min_length=1)
    model_version: str = Field(min_length=1)
    algorithm: str = Field(min_length=1)
    database: str | None = None
    database_version: str | None = None
    confidence: float = Field(ge=0, le=1)
    confidence_threshold: float = Field(ge=0, le=1)
    alternative_predictions: list[str] = Field(default_factory=list)
    evidence_ids: list[str] = Field(default_factory=list)
    assumptions: list[str] = Field(default_factory=list)
