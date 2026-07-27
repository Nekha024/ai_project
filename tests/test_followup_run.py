from interview_ai.interview_pipeline import (
    followup_pipeline
)

result = followup_pipeline(
    question="Tell me about your teamwork experience",
    answer="I worked in a team",
    confidence_score=0.6
)

print(result)