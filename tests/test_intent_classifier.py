from screening_ai.intent_classifier import (
    classify_intent
)

def test_intent():

    text = (
        "I have 3 years experience "
        "in python and django"
    )

    result = classify_intent(
        text
    )

    assert result == (
        "experience_info"
    )

    print(
        "Intent classification passed"
    )


if __name__ == "__main__":

    test_intent()