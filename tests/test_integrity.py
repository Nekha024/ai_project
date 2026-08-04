from integrity_ai.risk_engine import calculate_integrity_score


def test_integrity():

    score = calculate_integrity_score({
        "tab_switch": 2,
        "focus_loss": 1,
        "voice_detect": 0,
        "gaze_off": 2
    })

    assert score > 0


if __name__ == "__main__":
    test_integrity()
    print("Integrity Test Passed")