from ai_core.final_production_system import (
    normalize_score,
    smooth_scores,
    final_decision,
    production_pipeline,
       recruiter_output
)

from utils.final_error_handler import safe_run


def test_normalize_score():
    assert normalize_score(120) == 100.0
    assert normalize_score(-20) == 0.0
    assert normalize_score(80) == 80.0
    assert normalize_score("invalid") == 0.0


def test_smooth_scores():
    scores = {
        "ats": 90,
        "hr": 80
    }

    result = smooth_scores(scores)

    assert "ats" in result
    assert "hr" in result

    assert 0 <= result["ats"] <= 100
    assert 0 <= result["hr"] <= 100


def test_final_decision():
    assert final_decision(85) == "Selected"
    assert final_decision(70) == "Hold / Review"
    assert final_decision(40) == "Rejected"


def test_production_pipeline():
    result = production_pipeline(
        "C1",
        {
            "ats": 90,
            "hr": 80,
            "technical": 85
        }
    )

    assert result["candidate_id"] == "C1"
    assert "scores" in result
    assert "final_score" in result
    assert "decision" in result
    assert result["status"] == "production_ready"

    assert 0 <= result["final_score"] <= 100


def test_invalid_scores_are_handled():
    result = production_pipeline(
        "C2",
        {
            "ats": 120,
            "hr": -10,
            "technical": "invalid"
        }
    )

    assert result["final_score"] >= 0
    assert result["final_score"] <= 100


def test_empty_scores():
    result = production_pipeline("C3", {})

    assert result["final_score"] == 0.0
    assert result["decision"] == "Rejected"


def test_safe_run_success():
    result = safe_run(lambda: 10)

    assert result == 10


def test_safe_run_error():
    result = safe_run(
        lambda: 1 / 0,
        fallback="default"
    )

    assert result["status"] == "handled"
    assert result["fallback"] == "default"
    assert "error" in result

def test_recruiter_output():
    result = recruiter_output(
        "C20001",
        {
            "ats": 90,
            "hr": 85,
            "technical": 88
        },
        strengths=[
            "Strong technical skills",
            "Good communication"
        ],
        weaknesses=[
            "Minor optimization gaps"
        ],
        risks=[]
    )

    assert result["candidate_id"] == "C20001"
    assert result["decision"] == "Selected"
    assert result["confidence"] == "High"
    assert result["recommendation"] == "Proceed with offer"

    assert "summary" in result
    assert "strengths" in result["summary"]
    assert "weaknesses" in result["summary"]
    assert "risks" in result["summary"]