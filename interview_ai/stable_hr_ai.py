"""
Stable HR Evaluation Engine
"""

DECISION_THRESHOLDS = {
    "hire": 75,
    "consider": 55
}


def smooth_score(scores):
    """
    Removes extreme outliers and returns
    a stable average score.
    """

    if not scores:
        return 0

    average = sum(scores) / len(scores)

    filtered = [
        score
        for score in scores
        if abs(score - average) <= 20
    ]

    if filtered:
        return round(sum(filtered) / len(filtered), 2)

    return round(average, 2)


def stable_decision(score):

    if score >= DECISION_THRESHOLDS["hire"]:
        return "Hire"

    if score >= DECISION_THRESHOLDS["consider"]:
        return "Consider"

    return "Reject"


def stable_hr_evaluation(scores):

    stable_score = smooth_score(scores)

    return {
        "stable_score": stable_score,
        "decision": stable_decision(stable_score)
    }