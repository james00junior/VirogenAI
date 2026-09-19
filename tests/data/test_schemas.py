import pytest
from pydantic import ValidationError

from data.schemas.evidence import EvidenceRecord
from data.schemas.scenario import SimulationParameters, SimulationScenario
from data.schemas.results import SimulationPoint


def valid_parameters() -> SimulationParameters:
    return SimulationParameters(
        initial_tumour_cells=1_000.0,
        growth_rate_per_day=0.1,
        carrying_capacity=1_000_000.0,
        treatment_start_day=10.0,
        treatment_effect=0.5,
        resistance_fraction=0.1,
    )


def test_simulation_scenario_accepts_valid_parameters() -> None:
    scenario = SimulationScenario(
        name="baseline",
        duration_days=30.0,
        time_step_days=0.5,
        parameters=valid_parameters(),
    )

    scenario.validate_time_grid()
    assert scenario.model_name == "logistic_tumour_growth"


def test_simulation_scenario_rejects_invalid_parameter_range() -> None:
    with pytest.raises(ValidationError):
        SimulationParameters(
            initial_tumour_cells=1_000.0,
            growth_rate_per_day=0.1,
            carrying_capacity=1_000_000.0,
            treatment_start_day=10.0,
            treatment_effect=1.2,
            resistance_fraction=0.1,
        )


def test_simulation_scenario_rejects_large_time_step() -> None:
    scenario = SimulationScenario(
        name="invalid-grid",
        duration_days=10.0,
        time_step_days=20.0,
        parameters=valid_parameters(),
    )

    with pytest.raises(ValueError, match="time_step_days"):
        scenario.validate_time_grid()


def test_evidence_record_preserves_provenance_metadata() -> None:
    record = EvidenceRecord(
        evidence_id="doi:10.1000/example",
        title="Tumour growth study",
        source_type="peer_reviewed",
        doi="10.1000/example",
        authors=["Author A"],
        tags=["tumour-growth"],
    )

    assert record.evidence_id == record.doi
    assert record.source_type == "peer_reviewed"


def test_simulation_point_enforces_fraction_bounds() -> None:
    point = SimulationPoint(
        day=1.0,
        tumour_cells=500.0,
        viable_fraction=0.8,
        resistant_fraction=0.2,
    )

    assert point.viable_fraction + point.resistant_fraction == pytest.approx(1.0)
