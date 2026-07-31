from interview_ai.hr_scoring_engine import hr_scoring_pipeline
from ai_core.unified_scoring_engine import calculate_unified_score
from interview_ai.summary_generator import generate_interview_summary


DEFAULT_WEIGHTS = {
    "ats": 0.30,
    "screening": 0.30,
    "hr": 0.40
}


def run_hr_interview(
    candidate_id,
    answers,
    communication,
    behavior,
    ats_score=70,
    screening_score=75
):

    hr_result = hr_scoring_pipeline(
        answers,
        candidate_type="fresher"
    )

    final_score = calculate_unified_score(
        ats_score=ats_score,
        screening_score=screening_score,
        hr_score=hr_result["hr_score"],
        weights=DEFAULT_WEIGHTS
    )

    summary = generate_interview_summary(
        candidate_id,
        hr_result["details"],
        communication,
        behavior,
        answers
    )

    return {

        "candidate_id": candidate_id,

        "scores": {

            "ats": ats_score,

            "screening": screening_score,

            "hr": hr_result["hr_score"],

            "communication":
            communication["communication_score"],

            "confidence":
            behavior["confidence"]["confidence_score"],

            "behavior":
            behavior["behavioral_score"]

        },

        "final_score": round(final_score, 2),

        "decision": summary["decision"],

        "summary": summary

    }