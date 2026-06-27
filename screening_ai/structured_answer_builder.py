from screening_ai.answer_understanding_engine import (
    understand_answer
)


def build_structured_answers(
    responses
):

    structured = []

    for response in responses:

        structured.append(

            understand_answer(
                response["question_id"],
                response["answer"]
            )

        )

    return structured