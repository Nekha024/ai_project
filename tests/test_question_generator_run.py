from interview_ai.question_generator import (
    generate_questions
)

questions = generate_questions(
    "technical",
    "experienced"
)

print("\nGenerated Questions\n")

for i, question in enumerate(questions, start=1):
    print(f"{i}. {question}")