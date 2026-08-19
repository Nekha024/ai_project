from ai_core.release_ready_system import release_pipeline


result = release_pipeline(
    "C30001",
    {
        "ats": 120,
        "hr": -10,
        "technical": 85
    }
)

print("Zecpath AI - Release Ready Test")
print("--------------------------------")

print("Candidate ID:", result["candidate_id"])
print("Scores:", result["scores"])
print("Final Score:", result["final_score"])
print("Decision:", result["decision"])
print("Status:", result["status"])