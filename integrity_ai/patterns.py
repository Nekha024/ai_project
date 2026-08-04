"""
Pattern Recognition Rules
"""


def detect_patterns(events):

    patterns = []

    if (
        events.get("tab_switch", 0) > 3
        and events.get("focus_loss", 0) > 2
    ):
        patterns.append(
            "Possible external searching"
        )

    if (
        events.get("voice_detect", 0) > 2
    ):
        patterns.append(
            "Possible external assistance"
        )

    if (
        events.get("gaze_off", 0) > 5
    ):
        patterns.append(
            "Repeated gaze deviation"
        )

    return patterns