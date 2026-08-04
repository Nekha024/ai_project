"""
Normalize Scores
"""


def normalize_scores(scores):

    normalized = {}

    for key, value in scores.items():

        normalized[key] = max(min(value, 100), 0)

    return normalized