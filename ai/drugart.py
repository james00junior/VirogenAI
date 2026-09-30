"""Controlled AI orchestration boundary for DRUGART/VirogenAI."""
from dataclasses import dataclass, field
from typing import Protocol, Sequence

from data.schemas.provenance import PredictionProvenance


@dataclass(frozen=True)
class EvidenceItem:
    evidence_id: str
    title: str
    source: str
    excerpt: str


@dataclass(frozen=True)
class ResearchContext:
    question: str
    evidence: Sequence[EvidenceItem] = ()
    assumptions: Sequence[str] = ()


@dataclass
class DrugArtResearchState:
    context: ResearchContext
    candidate_ids: list[str] = field(default_factory=list)
    provenance: list[PredictionProvenance] = field(default_factory=list)
    recommendations: list[str] = field(default_factory=list)


class EvidenceRetriever(Protocol):
    def search(self, query: str, *, top_k: int = 10) -> list[EvidenceItem]: ...


def build_research_context(
    question: str, retriever: EvidenceRetriever, *, top_k: int = 10
) -> ResearchContext:
    if not question.strip():
        raise ValueError("question must not be empty")
    return ResearchContext(question=question, evidence=retriever.search(question, top_k=top_k))
