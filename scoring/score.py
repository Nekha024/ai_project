def calculate_skill_match(candidate_skills, required_skills):
    matched = set(candidate_skills) & set(required_skills)
    return len(matched) / len(required_skills) * 100


def calculate_experience_match(candidate_exp, required_exp):
    if candidate_exp >= required_exp:
        return 100
    return (candidate_exp / required_exp) * 100


def calculate_final_score(candidate, job):
    skill_score = calculate_skill_match(
        candidate["skills"], job["required_skills"]
    )

    exp_score = calculate_experience_match(
        candidate["experience_years"], job["experience_required"]
    )

    final_score = (0.7 * skill_score) + (0.3 * exp_score)

    return round(final_score, 2)