from ai_core.unified_scoring_engine import (
    calculate_unified_score,
    get_weights
)

from ai_core.hiring_fit import calculate_hiring_fit


def unified_scoring_pipeline(

        candidate_id,
        ats_score,
        screening_score,
        hr_score,
        candidate_type="fresher"

):

    weights = get_weights(candidate_type)

    final_score = calculate_unified_score(
        ats_score,
        screening_score,
        hr_score,
        weights
    )

    hiring_fit = calculate_hiring_fit(final_score)

    if final_score >= 75:
        decision = "Hire"

    elif final_score >= 55:
        decision = "Consider"

    else:
        decision = "Reject"

    return {

        "candidate_id": candidate_id,

        "scores": {

            "ats": ats_score,

            "screening": screening_score,

            "hr": hr_score

        },

        "weights_used": weights,

        "final_score": final_score,

        "decision": decision,

        "hiring_fit": hiring_fit,

        "explanation": {

            "ats": "Resume and skills matched job requirements.",

            "screening": "Screening responses evaluated successfully.",

            "hr": "HR interview communication and confidence analyzed."

        }

    }