def generate_screening_report(
    candidate_id,
    job_id,
    answers,
    scores,
    behavior_reports
):
    strengths = []
    risks = []
    missing = []
    key_answers = []

    salary = None
    availability = None
    confirmed_skills = set()

    for ans, score, behavior in zip(
        answers,
        scores,
        behavior_reports
    ):

        # -------------------------
        # Key Answer Summary
        # -------------------------
        key_answers.append({
            "question_id": ans["question_id"],
            "answer": ans["original_text"]
        })

        # -------------------------
        # Strength Detection
        # -------------------------
        if score["final_score"] >= 80:
            strengths.append(
                f"Strong answer in {ans['question_id']}"
            )

        # -------------------------
        # Risk Detection
        # -------------------------
        if (
            score["final_score"] < 50 or
            behavior["communication_strength"] == "Weak"
        ):
            risks.append(
                f"Weak response in {ans['question_id']}"
            )

        # -------------------------
        # Missing Data
        # -------------------------
        if (
            ans.get("is_vague", False)
            or
            ans.get("off_topic", False)
        ):
            missing.append(
                f"Incomplete answer in {ans['question_id']}"
            )

        # -------------------------
        # Highlights Extraction
        # -------------------------
        if ans.get("salary"):
            salary = ans["salary"]

        if ans.get("availability"):
            availability = ans["availability"]

        for skill in ans.get("skills", []):
            confirmed_skills.add(skill)

    # -------------------------
    # Final Score
    # -------------------------
    final_score = (
        sum(s["final_score"] for s in scores) / len(scores)
        if scores else 0
    )

    # -------------------------
    # Decision Logic
    # -------------------------
    if final_score >= 70:
        decision = "Proceed"
    elif final_score >= 50:
        decision = "Review"
    else:
        decision = "Reject"

    return {
        "candidate_id": candidate_id,
        "job_id": job_id,
        "final_score": round(final_score, 2),
        "decision": decision,
        "summary": {
            "strengths": strengths,
            "risks": risks,
            "missing_data": missing
        },
        "highlights": {
            "salary_expectation": salary,
            "availability": availability,
            "confirmed_skills": list(confirmed_skills)
        },
        "answers": key_answers
    }