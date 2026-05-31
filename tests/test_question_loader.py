import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from screening_ai.question_loader import load_questions

questions = load_questions(
    "data/hr_screening_dataset.json"
)

print(questions[:3])