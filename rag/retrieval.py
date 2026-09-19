"""Retrieval interfaces; embedding/vector implementation is added after inventory validation."""
from dataclasses import dataclass
from typing import Protocol

@dataclass(frozen=True)
class RetrievedEvidence:
    document_id: str
    text: str
    score: float
    domain: str
    source: str

class Retriever(Protocol):
    def search(self, query: str, *, domain: str | None = None, top_k: int = 5) -> list[RetrievedEvidence]: ...
