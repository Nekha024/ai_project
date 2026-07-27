from interview_ai.aptitude_scoring import (
    calculate_aptitude_score
)


def test_aptitude():

    result = calculate_aptitude_score(

        "First I analyze then solve"

    )

    assert result["aptitude_score"] > 0