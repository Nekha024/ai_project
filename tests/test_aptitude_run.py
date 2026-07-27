from interview_ai.aptitude_pipeline import (
    aptitude_pipeline
)

text = (
    "First I analyze the problem, "
    "then I plan a solution, "
    "finally I prioritize the work "
    "and execute it carefully."
)

result = aptitude_pipeline(

    text,

    "deadline_pressure"

)

print(result)