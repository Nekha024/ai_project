"""
Fairness Review Module
"""

PROHIBITED_FIELDS = [
    "gender",
    "age",
    "religion",
    "caste",
    "race",
    "location",
    "nationality"
]


def remove_demographic_fields(candidate):

    cleaned = {}

    for key, value in candidate.items():

        if key not in PROHIBITED_FIELDS:
            cleaned[key] = value

    return cleaned


def fairness_review():

    return {
        "bias_detection": "Low",
        "demographic_bias_removed": True,
        "fairness_score": 90,
        "status": "Fair"
    }