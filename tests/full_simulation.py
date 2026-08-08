import random


def simulate_candidate():
    return {
        "ats": random.randint(60, 90),
        "screening": random.randint(60, 85),
        "hr": random.randint(65, 90),
        "technical": random.randint(60, 95),
        "machine_test": random.randint(60, 95)
    }


def calculate_final_score(scores):
    return round(sum(scores.values()) / len(scores), 2)


def make_decision(final_score):
    if final_score >= 75:
        return "Selected"
    elif final_score >= 60:
        return "Hold / Review"
    return "Rejected"


def simulate_full_candidate(candidate_id):
    scores = simulate_candidate()

    final_score = calculate_final_score(scores)
    decision = make_decision(final_score)

    return {
        "candidate_id": candidate_id,
        "scores": scores,
        "behavior": {
            "risk_level": random.choice(
                ["Low Risk", "Low Risk", "Moderate Risk"]
            )
        },
        "integrity": {
            "risk_level": random.choice(
                ["Low Risk", "Low Risk", "Moderate Risk"]
            )
        },
        "final_score": final_score,
        "decision": decision
    }


def run_full_simulation(n=50):
    results = []

    for i in range(1, n + 1):
        candidate_id = f"C{20000 + i}"
        candidate = simulate_full_candidate(candidate_id)
        results.append(candidate)

    return results


if __name__ == "__main__":
    results = run_full_simulation(10)

    for result in results:
        print("\n" + "=" * 50)
        print("Candidate:", result["candidate_id"])
        print("Scores:", result["scores"])
        print("Behavior:", result["behavior"])
        print("Integrity:", result["integrity"])
        print("Final Score:", result["final_score"])
        print("Decision:", result["decision"])