from integrity_ai.detection_logic import detect_malpractice
from integrity_ai.risk_engine import (
    calculate_integrity_score,
    risk_flagging
)
from integrity_ai.warning_system import generate_warning
from integrity_ai.integration import combined_risk
from integrity_ai.patterns import detect_patterns


events = {
    "tab_switch": 4,
    "focus_loss": 2,
    "voice_detect": 1,
    "gaze_off": 6
}

behavior_score = 78


flags = detect_malpractice(events)

integrity_score = calculate_integrity_score(events)

risk = risk_flagging(integrity_score)

warnings = generate_warning(events)

patterns = detect_patterns(events)

combined = combined_risk(
    behavior_score,
    integrity_score
)


result = {
    "candidate_id": "C4001",
    "integrity_score": integrity_score,
    "combined_score": combined,
    "risk_level": risk,
    "flags": flags,
    "warnings": warnings,
    "patterns": patterns
}

print(result)