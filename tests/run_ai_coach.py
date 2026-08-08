from future.ai_coach import generate_feedback

scores = {
    "communication": 60,
    "technical": 80,
    "confidence": 50
}

feedback = generate_feedback(scores)

print("AI Coaching Suggestions:")

for suggestion in feedback:
    print("-", suggestion)