"""
Behavior + Integrity Integration
"""


def combined_risk(behavior_score, integrity_score):

    final_score = (
        behavior_score * 0.40 +
        integrity_score * 0.60
    )

    return round(final_score, 2)