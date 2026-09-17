"""Validated simulation scenario schema.

This is intentionally independent of any solver implementation.
"""

from pydantic import BaseModel, Field


class SimulationParameters(BaseModel):
    """Minimal parameters for the first tumour-growth model."""

    initial_tumour_cells: float = Field(gt=0)
    growth_rate_per_day: float = Field(gt=0)
    carrying_capacity: float = Field(gt=0)
    treatment_start_day: float = Field(ge=0)
    treatment_effect: float = Field(ge=0, le=1)
    resistance_fraction: float = Field(ge=0, le=1)


class SimulationScenario(BaseModel):
    """A reproducible, versionable simulation scenario."""

    name: str = Field(min_length=1, max_length=200)
    model_name: str = Field(default="logistic_tumour_growth", min_length=1)
    model_version: str = Field(default="0.1.0", min_length=1)
    duration_days: float = Field(gt=0)
    time_step_days: float = Field(gt=0)
    parameters: SimulationParameters

    def validate_time_grid(self) -> None:
        """Validate that the requested duration is compatible with the time step."""
        if self.time_step_days > self.duration_days:
            raise ValueError("time_step_days must not exceed duration_days")
