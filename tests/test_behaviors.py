from interview_ai.behavior_analyzer import analyze_behavior


def test_behavior():

    result = analyze_behavior(
        "I am confident",
        5
    )

    assert result["behavioral_score"] > 0