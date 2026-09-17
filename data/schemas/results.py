"""Scientific simulation result schemas."""

from pydantic import BaseModel, Field


class SimulationPoint(BaseModel):
    """One point in a simulation time series."""

    day: float = Field(ge=0)
    tumour_cells: float = Field(ge=0)
    viable_fraction: float = Field(ge=0, le=1)
    resistant_fraction: float = Field(ge=0, le=1)


class SimulationResult(BaseModel):
    """Reproducible output envelope for a simulation run."""

    model_name: str
    model_version: str
    scenario_name: str
    points: list[SimulationPoint]
