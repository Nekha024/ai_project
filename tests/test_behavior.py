from screening_ai.behavior_report import generate_behavior_report

def test_behavior():
    text = "I am confident and experienced in Python"
    result = generate_behavior_report(text, 5)

    assert "communication_strength" in result
    assert result["communication_strength"] in [
        "Strong", "Moderate", "Weak"
    ]