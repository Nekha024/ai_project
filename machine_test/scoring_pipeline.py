from machine_test.evaluation_logic import calculate_task_score
from machine_test.time_scoring import time_score


def machine_test_pipeline(data):

    score = calculate_task_score(
        data["execution_results"]["passed"],
        data["execution_results"]["total"],
        data["execution_results"]["runtime"],
        data["code_snapshot"],
        data["attempts"]
    )

    time_factor = time_score(
        data["time_taken"],
        30
    )

    final_score = (
        score["task_score"] * 0.80 +
        time_factor * 100 * 0.20
    )

    if final_score >= 80:
        decision = "Excellent Performance"

    elif final_score >= 65:
        decision = "Good Performance"

    elif final_score >= 50:
        decision = "Average"

    else:
        decision = "Needs Improvement"

    return {
        "candidate_id": data["candidate_id"],
        "task_id": data["task_id"],
        "time_score": round(time_factor * 100, 2),
        "final_score": round(final_score, 2),
        "decision": decision,
        "details": score
    }