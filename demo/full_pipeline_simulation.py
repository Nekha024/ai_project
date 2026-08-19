# Day 63 - Demo Full Pipeline Simulation

def run_demo_pipeline(candidate):
    scores = {
        "C001": {
            "final_score": 85,
            "decision": "Selected"
        },
        "C002": {
            "final_score": 68,
            "decision": "Hold / Review"
        },
        "C003": {
            "final_score": 45,
            "decision": "Rejected"
        }
    }

    return {
        "candidate_id": candidate,
        "result": scores.get(candidate)
    }


if __name__ == "__main__":
    for candidate in ["C001", "C002", "C003"]:
        print(run_demo_pipeline(candidate))