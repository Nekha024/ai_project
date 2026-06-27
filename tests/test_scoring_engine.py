from screening_ai.answer_understanding_engine import process_answer
from screening_ai.scoring_engine import score_answer

answer = process_answer(
    "Q3",
    "I have 3 years experience in Python and Django"
)

result = score_answer(answer)

print(result)