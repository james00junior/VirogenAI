import pytest

from analysis.experimental import percent_inhibition, validate_fraction


def test_percent_inhibition() -> None:
    assert percent_inhibition(100, 25) == pytest.approx(75.0)


def test_percent_inhibition_rejects_zero_control() -> None:
    with pytest.raises(ValueError):
        percent_inhibition(0, 10)


def test_validate_fraction() -> None:
    assert validate_fraction(0.5) == 0.5


def test_validate_fraction_rejects_invalid_value() -> None:
    with pytest.raises(ValueError):
        validate_fraction(1.1)
