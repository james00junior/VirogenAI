import pytest
from pydantic import ValidationError

from data.schemas.provenance import PredictionProvenance


def test_prediction_provenance_requires_valid_confidence():
    record = PredictionProvenance(
        model_name="candidate-model",
        model_version="1.0.0",
        algorithm="gradient_boosting",
        confidence=0.91,
        confidence_threshold=0.80,
        evidence_ids=["E001"],
    )
    assert record.confidence >= record.confidence_threshold


def test_prediction_provenance_rejects_invalid_confidence():
    with pytest.raises(ValidationError):
        PredictionProvenance(
            model_name="candidate-model",
            model_version="1.0.0",
            algorithm="gradient_boosting",
            confidence=1.5,
            confidence_threshold=0.8,
        )
