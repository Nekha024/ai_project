from tests.full_simulation import run_full_simulation


def test_simulation():
    results = run_full_simulation(10)

    assert len(results) == 10

    for candidate in results:
        assert "candidate_id" in candidate
        assert "scores" in candidate
        assert "final_score" in candidate
        assert "decision" in candidate

        assert 0 <= candidate["final_score"] <= 100