from interview_ai.followup_engine import (
    detect_answer_quality
)


def test_followup():

    result = detect_answer_quality(
        "I worked"
    )

    assert result == "too_short"