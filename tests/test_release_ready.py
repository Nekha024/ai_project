from ai_core.release_ready_system import (
    safe_value,
    validate_scores,
    final_aggregate,
    final_decision,
    release_pipeline
)


# --------------------------------
# Safe Value Tests
# --------------------------------

def test_safe_value_normal():
    assert safe_value(80) == 80


def test_safe_value_overflow():
    assert safe_value(120) == 100


def test_safe_value_negative():
    assert safe_value(-10) == 0


def test_safe_value_invalid():
    assert safe_value("invalid") == 0


# --------------------------------
# Score Validation Tests
# --------------------------------

def test_validate_scores():
    scores = {
        "ats": 120,
        "hr": -10,
        "technical": 85
    }

    result = validate_scores(scores)

    assert result["ats"] == 100
    assert result["hr"] == 0
    assert result["technical"] == 85


# --------------------------------
# Aggregation Tests
# --------------------------------

def test_final_aggregate():
    scores = {
        "ats": 80,
        "hr": 70,
        "technical": 90
    }

    result = final_aggregate(scores)

    assert result == 80


def test_empty_scores():
    assert final_aggregate({}) == 0.0


# --------------------------------
# Decision Tests
# --------------------------------

def test_selected_decision():
    assert final_decision(85) == "Selected"


def test_hold_decision():
    assert final_decision(70) == "Hold / Review"


def test_rejected_decision():
    assert final_decision(45) == "Rejected"


# --------------------------------
# Full Release Pipeline
# --------------------------------

def test_release_pipeline():
    result = release_pipeline(
        "C1",
        {
            "ats": 120,
            "hr": -10,
            "technical": 85
        }
    )

    assert result["candidate_id"] == "C1"
    assert result["scores"]["ats"] == 100
    assert result["scores"]["hr"] == 0
    assert result["scores"]["technical"] == 85

    assert result["final_score"] == 61.67
    assert result["decision"] == "Hold / Review"
    assert result["status"] == "release_ready"


# --------------------------------
# Edge Case Tests
# --------------------------------

def test_invalid_scores_input():
    result = release_pipeline("C2", None)

    assert result["scores"] == {}
    assert result["final_score"] == 0.0
    assert result["decision"] == "Rejected"


def test_mixed_invalid_scores():
    result = release_pipeline(
        "C3",
        {
            "ats": "invalid",
            "hr": None,
            "technical": 90
        }
    )

    assert result["scores"]["ats"] == 0
    assert result["scores"]["hr"] == 0
    assert result["scores"]["technical"] == 90