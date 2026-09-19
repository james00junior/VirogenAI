"""Deterministic helpers for experimental antiviral analysis."""
from __future__ import annotations

import numpy as np


def percent_inhibition(control: float, treatment: float) -> float:
    """Calculate inhibition relative to a control measurement."""
    if control <= 0:
        raise ValueError("control must be greater than zero")
    return float((control - treatment) / control * 100.0)


def validate_fraction(value: float) -> float:
    """Validate and return a fraction in [0, 1]."""
    value = float(value)
    if not 0 <= value <= 1:
        raise ValueError("fraction must be between 0 and 1")
    return value
