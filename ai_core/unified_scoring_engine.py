# -------------------------------
# Default Cross-Round Weights
# -------------------------------

DEFAULT_WEIGHTS = {
    "ats": 0.30,
    "screening": 0.30,
    "hr": 0.40
}

# -------------------------------
# Role-Based Weights
# -------------------------------

ROLE_BASED_WEIGHTS = {

    "fresher": {
        "ats": 0.25,
        "screening": 0.35,
        "hr": 0.40
    },

    "experienced": {
        "ats": 0.35,
        "screening": 0.25,
        "hr": 0.40
    },

    "technical": {
        "ats": 0.40,
        "screening": 0.30,
        "hr": 0.30
    },

    "non_technical": {
        "ats": 0.20,
        "screening": 0.30,
        "hr": 0.50
    }

}


def get_weights(candidate_type=None):
    return ROLE_BASED_WEIGHTS.get(
        candidate_type,
        DEFAULT_WEIGHTS
    )


# -------------------------------
# Unified Score
# -------------------------------

def calculate_unified_score(
        ats_score,
        screening_score,
        hr_score,
        weights):

    score = (

        ats_score * weights["ats"] +

        screening_score * weights["screening"] +

        hr_score * weights["hr"]

    )

    return round(score, 2)