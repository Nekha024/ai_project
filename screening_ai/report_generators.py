def generate_screening_report(
    candidate_id,
    job_id,
    answers,
    scores,
    behavior_reports
):

    final_score = 0

    if scores:
        final_score = sum(
            s["final_score"] for s in scores
        ) / len(scores)

    decision = "Proceed" if final_score >= 70 else "Reject"

    strengths = []
    risks = []
    missing_data = []

    for score in scores:
        if score["final_score"] >= 80:
            strengths.append(
                f"Strong answer in {score['question_id']}"
            )

    confirmed_skills = []
    salary = None
    availability = None

    for answer in answers:

        confirmed_skills.extend(
            answer.get("skills", [])
        )

        salary = answer.get(
            "salary",
            salary
        )

        availability = answer.get(
            "availability",
            availability
        )

        if answer.get("is_vague"):
            risks.append(
                f"Vague answer in {answer['question_id']}"
            )

        if answer.get("off_topic"):
            risks.append(
                f"Off-topic answer in {answer['question_id']}"
            )

    return {
        "candidate_id": candidate_id,
        "job_id": job_id,
        "final_score": round(final_score, 2),
        "decision": decision,
        "summary": {
            "strengths": strengths,
            "risks": risks,
            "missing_data": missing_data
        },
        "highlights": {
            "salary_expectation": salary,
            "availability": availability,
            "confirmed_skills": list(
                set(confirmed_skills)
            )
        },
        "answers": answers
    }