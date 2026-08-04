from ai_core.cross_round_engine import (
    calculate_final_score,
    get_weights
)

from ai_core.hiring_fit_calculator import calculate_hiring_fit

from ai_core.normalization import normalize_scores


def aggregation_pipeline(
    candidate_id,
    scores,
    role_type="technical"
):

    normalized_scores = normalize_scores(scores)

    weights = get_weights(role_type)

    final_score = calculate_final_score(
        normalized_scores,
        weights
    )

    fit = calculate_hiring_fit(final_score)

    if final_score >= 75:
        decision = "Hire"

    elif final_score >= 55:
        decision = "Consider"

    else:
        decision = "Reject"

    return {

        "candidate_id": candidate_id,

        "scores": normalized_scores,

        "weights": weights,

        "final_score": final_score,

        "decision": decision,

        "hiring_fit": fit

    }