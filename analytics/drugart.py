"""Advanced analytics primitives for the DRUGART Phase 3 workflow."""
from dataclasses import dataclass
from math import isfinite
from typing import Sequence


@dataclass(frozen=True)
class CandidateMetrics:
    candidate_id: str
    potency: float
    selectivity: float
    stability: float
    toxicity_risk: float
    manufacturability: float

    def __post_init__(self) -> None:
        if not self.candidate_id:
            raise ValueError("candidate_id must not be empty")
        values = (self.potency, self.selectivity, self.stability,
                  self.toxicity_risk, self.manufacturability)
        if not all(isfinite(value) for value in values):
            raise ValueError("candidate metrics must be finite")
        if self.toxicity_risk < 0:
            raise ValueError("toxicity_risk must be non-negative")


def dominates(left: CandidateMetrics, right: CandidateMetrics) -> bool:
    """Return True when left is no worse on every objective and better on one."""
    left_values = (left.potency, left.selectivity, left.stability,
                   -left.toxicity_risk, left.manufacturability)
    right_values = (right.potency, right.selectivity, right.stability,
                    -right.toxicity_risk, right.manufacturability)
    return all(a >= b for a, b in zip(left_values, right_values)) and any(
        a > b for a, b in zip(left_values, right_values)
    )


def pareto_frontier(candidates: Sequence[CandidateMetrics]) -> list[CandidateMetrics]:
    """Return non-dominated candidates in input order."""
    return [
        candidate
        for candidate in candidates
        if not any(
            dominates(other, candidate)
            for other in candidates
            if other != candidate
        )
    ]


def normalise_metrics(
    candidates: Sequence[CandidateMetrics],
) -> dict[str, dict[str, float]]:
    """Return min-max normalised objectives for transparent downstream analysis."""
    if not candidates:
        return {}
    columns = {
        "potency": [c.potency for c in candidates],
        "selectivity": [c.selectivity for c in candidates],
        "stability": [c.stability for c in candidates],
        "toxicity_risk": [c.toxicity_risk for c in candidates],
        "manufacturability": [c.manufacturability for c in candidates],
    }
    result = {c.candidate_id: {} for c in candidates}
    for name, values in columns.items():
        low, high = min(values), max(values)
        for candidate in candidates:
            value = getattr(candidate, name)
            scaled = 0.5 if high == low else (value - low) / (high - low)
            result[candidate.candidate_id][name] = (
                1.0 - scaled if name == "toxicity_risk" else scaled
            )
    return result
