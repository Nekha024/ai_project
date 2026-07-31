from ai_core.unified_scoring_engine import (
    calculate_unified_score
)

from ai_core.unified_pipeline import (
    unified_scoring_pipeline
)


def test_unified_score():

    score = calculate_unified_score(

        80,

        70,

        90,

        {

            "ats": 0.30,

            "screening": 0.30,

            "hr": 0.40

        }

    )

    assert score > 0


def test_pipeline():

    result = unified_scoring_pipeline(

        "C1",

        80,

        75,

        85,

        "fresher"

    )

    assert result["decision"] in [
        "Hire",
        "Consider",
        "Reject"
    ]

    assert "final_score" in result

    assert "hiring_fit" in result