import json
import random
import os


def load_question_bank():
    current_dir = os.path.dirname(__file__)
    path = os.path.join(current_dir, "question_bank.json")

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def generate_questions(role_type, experience_level):
    qb = load_question_bank()

    questions = []

    questions.extend(
        qb["categories"]["introduction"][experience_level]
    )

    for category in [
        "strengths_weaknesses",
        "teamwork",
        "career_goals",
        "availability"
    ]:
        questions.extend(
            qb["categories"][category]["common"]
        )

    questions.extend(
        qb["role_based"][role_type]
    )

    return random.sample(
        questions,
        min(6, len(questions))
    )


if __name__ == "__main__":
    result = generate_questions(
        "technical",
        "experienced"
    )

    for i, question in enumerate(result, start=1):
        print(f"Q{i}. {question}")