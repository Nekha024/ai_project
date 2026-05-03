from ats_engine.skill_extractor import extract_skills_with_confidence


def role_similarity(role_text, job_description):
    role_skills = extract_skills_with_confidence(role_text)
    job_skills = extract_skills_with_confidence(job_description)

    if not role_skills or not job_skills:
        return 0

    match = set(role_skills.keys()) & set(job_skills.keys())

    return len(match) / len(job_skills)


def compute_experience_relevance(experiences, job_description):
    scores = []

    for exp in experiences:
        score = role_similarity(exp["title"], job_description)

        # weight by duration
        weighted_score = score * (exp["duration_months"] / 12)

        scores.append(weighted_score)

    return round(sum(scores), 2)