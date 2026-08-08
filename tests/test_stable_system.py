from ai_core.stable_system import (
    safe_score,
    stable_aggregate,
    stable_decision,
    stable_pipeline
)


def test_safe_score():
    assert safe_score(120) == 100
    assert safe_score(-10) == 0
    assert safe_score("invalid") == 0
    assert safe_score(80) == 80


def test_stable_aggregate():
    result = stable_aggregate({
        "ats": 120,
        "hr": -10
    })

    assert result == 50


def test_stable_decision():
    assert stable_decision(80) == "Selected"
    assert stable_decision(60) == "Hold / Review"
    assert stable_decision(40) == "Rejected"


def test_stable_pipeline():
    result = stable_pipeline(
        "C1",
        {
            "ats": 120,
            "hr": -10
        }
    )

    assert result["final_score"] <= 100
    assert result["status"] == "stable"
    assert "decision" in result