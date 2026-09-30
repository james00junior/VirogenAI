from analytics.drugart import CandidateMetrics, dominates, normalise_metrics, pareto_frontier


def test_dominance_and_pareto_frontier():
    strong = CandidateMetrics("strong", 90, 90, 90, 5, 90)
    weaker = CandidateMetrics("weaker", 80, 80, 80, 10, 80)
    tradeoff = CandidateMetrics("tradeoff", 95, 70, 80, 12, 95)

    assert dominates(strong, weaker)
    assert not dominates(weaker, strong)
    assert [c.candidate_id for c in pareto_frontier([strong, weaker, tradeoff])] == [
        "strong",
        "tradeoff",
    ]


def test_normalisation_inverts_toxicity_risk():
    low = CandidateMetrics("low", 50, 50, 50, 2, 50)
    high = CandidateMetrics("high", 100, 100, 100, 10, 100)
    values = normalise_metrics([low, high])

    assert values["high"]["potency"] == 1.0
    assert values["low"]["toxicity_risk"] == 1.0
