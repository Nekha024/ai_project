def detect_behavior_risk(score):

    if score >= 85:
        return "Highly Focused"

    elif score >= 70:
        return "Good Engagement"

    elif score >= 50:
        return "Moderate"

    return "Distracted / High Risk"