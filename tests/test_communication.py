from interview_ai.communication_engine import (
    calculate_communication_score
)


def test_communication():

    result = calculate_communication_score(
        "I worked on several backend projects using Python."
    )

    assert result["communication_score"] > 0