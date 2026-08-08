from ai_core.stable_system import stable_pipeline

result = stable_pipeline(
    "C1",
    {
        "ats": 120,
        "hr": -10,
        "technical": 85
    }
)

print(result)