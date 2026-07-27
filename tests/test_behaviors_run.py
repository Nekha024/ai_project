from interview_ai.behavior_analyzer import analyze_behavior

text = (
    "I think I am confident but maybe "
    "I need improvement."
)

duration = 6

result = analyze_behavior(
    text,
    duration
)

print("\nBehavior Analysis Output\n")
print(result)