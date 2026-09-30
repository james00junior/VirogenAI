"""Uncertainty analytics for DRUGART experiments."""
from dataclasses import dataclass
from statistics import mean
from typing import Sequence


@dataclass(frozen=True)
class Interval:
    estimate: float
    lower: float
    upper: float
    confidence: float


def bootstrap_mean_interval(
    values: Sequence[float],
    *,
    confidence: float = 0.95,
    samples: int = 2000,
    seed: int = 42,
) -> Interval:
    """Estimate a reproducible percentile bootstrap interval for a mean."""
    if not values:
        raise ValueError("values must not be empty")
    if not 0 < confidence < 1:
        raise ValueError("confidence must be between 0 and 1")
    if samples < 100:
        raise ValueError("samples must be at least 100")

    import random

    rng = random.Random(seed)
    n = len(values)
    bootstrap_means = [
        mean(values[rng.randrange(n)] for _ in range(n))
        for _ in range(samples)
    ]
    bootstrap_means.sort()
    alpha = (1.0 - confidence) / 2.0

    def percentile(p: float) -> float:
        index = p * (len(bootstrap_means) - 1)
        low = int(index)
        high = min(low + 1, len(bootstrap_means) - 1)
        weight = index - low
        return bootstrap_means[low] * (1 - weight) + bootstrap_means[high] * weight

    return Interval(
        estimate=mean(values),
        lower=percentile(alpha),
        upper=percentile(1 - alpha),
        confidence=confidence,
    )
