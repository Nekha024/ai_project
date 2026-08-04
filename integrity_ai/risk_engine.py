"""
Integrity Risk Scoring
"""


def calculate_integrity_score(events):

    score = 100

    score -= events.get("tab_switch", 0) * 5
    score -= events.get("focus_loss", 0) * 3
    score -= events.get("voice_detect", 0) * 10
    score -= events.get("gaze_off", 0) * 4

    return max(score, 0)


def risk_flagging(score):

    if score >= 75:
        return "Low Risk"

    elif score >= 50:
        return "Moderate Risk"

    return "High Risk"