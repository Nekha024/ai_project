def generate_natural_summary(
    strengths,
    weaknesses,
    risks,
    culture_fit,
    decision
):

    return (
        f"The candidate demonstrates "
        f"{', '.join(strengths[:2]) if strengths else 'some strengths'}. "
        f"However, there are concerns such as "
        f"{', '.join(weaknesses[:2]) if weaknesses else 'minor weaknesses'}. "
        f"Risk factors include "
        f"{', '.join(risks) if risks else 'no major risks'}. "
        f"Cultural fit is assessed as {culture_fit}. "
        f"Final Recommendation: {decision}."
    )


def generate_interview_summary(
    candidate_id,
    hr_scores,
    communication,
    behavior,
    answers
):

    strengths = []
    weaknesses = []
    risks = []
    inconsistencies = []

    # -----------------------------
    # HR Score Analysis
    # -----------------------------
    for item in hr_scores:

        if item["final_score"] >= 80:

            strengths.append(
                f"Strong performance in {item['question_id']}"
            )

        elif item["final_score"] < 50:

            weaknesses.append(
                f"Weak response in {item['question_id']}"
            )

    # -----------------------------
    # Communication
    # -----------------------------
    comm_score = communication.get(
        "communication_score",
        0
    )

    if comm_score >= 80:

        strengths.append(
            "Excellent communication skills"
        )

    elif comm_score < 50:

        weaknesses.append(
            "Poor communication clarity"
        )

    # -----------------------------
    # Behavior
    # -----------------------------
    confidence = behavior.get(
        "confidence",
        {}
    ).get(
        "confidence_score",
        0
    )

    if confidence < 60:

        risks.append(
            "Low confidence detected"
        )

    if behavior.get("contradiction"):

        inconsistencies.append(
            "Contradictory statements observed"
        )

    # -----------------------------
    # Cultural Fit
    # -----------------------------
    culture_fit = "Good"

    text = str(answers).lower()

    if "team" in text:

        strengths.append(
            "Shows teamwork orientation"
        )

    else:

        culture_fit = "Moderate"

    # -----------------------------
    # Overall Score
    # -----------------------------
    if hr_scores:

        hr_average = sum(
            item["final_score"]
            for item in hr_scores
        ) / len(hr_scores)

    else:

        hr_average = 0

    overall_score = (

        comm_score * 0.30 +

        behavior.get(
            "behavioral_score",
            0
        ) * 0.30 +

        hr_average * 0.40

    )

    if overall_score >= 75:

        decision = "Strong Hire"

    elif overall_score >= 55:

        decision = "Consider"

    else:

        decision = "Reject"

    return {

        "candidate_id": candidate_id,

        "overall_score": round(
            overall_score,
            2
        ),

        "decision": decision,

        "summary": {

            "strengths": strengths,

            "weaknesses": weaknesses,

            "risks": risks,

            "inconsistencies": inconsistencies,

            "cultural_fit": culture_fit

        },

        "natural_language_summary":

            generate_natural_summary(

                strengths,

                weaknesses,

                risks,

                culture_fit,

                decision

            )

    }