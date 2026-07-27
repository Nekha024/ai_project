from interview_ai.hr_scoring_engine import (
    hr_scoring_pipeline
)


def test_hr_score():

    result = hr_scoring_pipeline(
        [],
        "fresher"
    )

    assert "hr_score" in result