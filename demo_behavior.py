from behavior_ai.signal_mapping import calculate_behavior_score
from behavior_ai.risk_detector import detect_behavior_risk

signals = {
    "eye_focus": 0.8,
    "head_stability": 0.7,
    "engagement": 0.9,
    "distraction": 0.2
}

score = calculate_behavior_score(signals)
risk = detect_behavior_risk(score)

print("Behavior Score :", score)
print("Behavior Level :", risk)