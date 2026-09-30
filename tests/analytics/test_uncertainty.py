from analytics.uncertainty import bootstrap_mean_interval


def test_bootstrap_interval_is_reproducible():
    values = [1.0, 2.0, 3.0, 4.0]
    first = bootstrap_mean_interval(values, samples=500, seed=42)
    second = bootstrap_mean_interval(values, samples=500, seed=42)

    assert first == second
    assert first.lower <= first.estimate <= first.upper
