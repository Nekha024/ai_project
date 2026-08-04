from behavior_ai.signal_mapping import calculate_behavior_score

def test_behavior_score():

    result = calculate_behavior_score({
        "eye_focus":0.7,
        "head_stability":0.7,
        "engagement":0.8,
        "distraction":0.3
    })

    assert result > 0