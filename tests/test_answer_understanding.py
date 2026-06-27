from screening_ai.answer_understanding_engine import (
    understand_answer
)

def test_answer_understanding():

    result = understand_answer(

        "Q1",

        "I have 3 years experience in Python Django and expect 8 LPA salary and can join immediately"

    )

    assert (
        result["experience_years"]
        == 3
    )

    assert (
        "python"
        in result["skills"]
    )

    assert (
        result["availability"]
        == "Immediate"
    )

    print(
        "Answer understanding passed"
    )


if __name__ == "__main__":

    test_answer_understanding()