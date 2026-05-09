import re


# -------------------------------
# Score Normalization
# -------------------------------

def normalize_scores(candidate_scores):

    scores = [
        c["final_score"]
        for c in candidate_scores
    ]

    min_score = min(scores)
    max_score = max(scores)

    # Avoid division by zero
    if max_score == min_score:
        return candidate_scores

    for c in candidate_scores:

        c["normalized_score"] = round(

            (
                (
                    c["final_score"] - min_score
                )
                /
                (
                    max_score - min_score
                )
            ) * 100,

            2
        )

    return candidate_scores


# -------------------------------
# Mask Sensitive Data
# -------------------------------

def mask_sensitive_data(candidate):

    sensitive_fields = [
        "name",
        "gender",
        "age",
        "photo",
        "location"
    ]

    for field in sensitive_fields:

        if field in candidate:
            candidate[field] = "MASKED"

    return candidate


# -------------------------------
# Keyword Bias Reduction
# -------------------------------

def reduce_keyword_bias(
    skill_score,
    semantic_score
):

    adjusted_score = (
        0.6 * semantic_score
        +
        0.4 * skill_score
    )

    return round(adjusted_score, 2)


# -------------------------------
# Generate Fair Score
# -------------------------------

def generate_fair_score(candidate):

    skill_score = candidate.get(
        "skill_score",
        0
    )

    semantic_score = candidate.get(
        "semantic_score",
        0
    )

    fair_score = reduce_keyword_bias(
        skill_score,
        semantic_score
    )

    candidate["fair_score"] = fair_score

    return candidate