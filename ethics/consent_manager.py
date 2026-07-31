"""
Consent Management Module
"""


def collect_consent(
    candidate_id,
    ai_evaluation=True,
    data_processing=True,
    audio_recording=False
):
    return {
        "candidate_id": candidate_id,
        "consent": {
            "ai_evaluation": ai_evaluation,
            "data_processing": data_processing,
            "audio_recording": audio_recording
        },
        "status": (
            "Accepted"
            if ai_evaluation and data_processing
            else "Rejected"
        )
    }


def has_valid_consent(consent):

    return (
        consent["consent"]["ai_evaluation"]
        and consent["consent"]["data_processing"]
    )