from interview_ai.communication_engine import (
    calculate_communication_score
)

text = (
    "I have experience in Python because "
    "I worked on backend systems and REST APIs."
)

result = calculate_communication_score(text)

print("\nCommunication Score Output\n")
print(result)
