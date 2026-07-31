"""
Explainability Engine
"""


def generate_explanation(
    ats_score,
    screening_score,
    hr_score
):

    return {
        "ats": (
            "Strong resume match"
            if ats_score >= 75
            else "Needs improvement"
        ),

        "screening": (
            "Good answer relevance"
            if screening_score >= 70
            else "Average responses"
        ),

        "hr": (
            "Strong communication and confidence"
            if hr_score >= 75
            else "Further evaluation recommended"
        )
    }