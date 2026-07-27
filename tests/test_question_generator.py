from interview_ai.question_generator import (
    generate_questions
)


def test_question_generation():

    questions = generate_questions(
        "technical",
        "experienced"
    )

    assert len(questions) > 0