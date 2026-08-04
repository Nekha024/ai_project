from ai_core.decision_engine import generate_decision


def test_decision():

    decision, score = generate_decision(85)

    assert decision == "Selected"


if __name__ == "__main__":

    test_decision()

    print("Decision Test Passed")