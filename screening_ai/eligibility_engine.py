# screening_ai/eligibility_engine.py

DEFAULT_RULES = {
    "min_ats_score": 70,
    "mandatory_skills": [],
    "min_experience": 0,
    "max_experience": 10,
    "allowed_locations": [],
    "availability_required": False
}


def safe_value(value, default):
    return value if value is not None else default


# -------------------------------
# Skill Check
# -------------------------------
def check_mandatory_skills(candidate_skills, required_skills):

    if not required_skills:
        return True

    candidate_skills = [s.lower() for s in candidate_skills]
    required_skills = [s.lower() for s in required_skills]

    return all(skill in candidate_skills for skill in required_skills)


# -------------------------------
# Experience Check
# -------------------------------
def check_experience(candidate_exp, min_exp, max_exp):

    return min_exp <= candidate_exp <= max_exp


# -------------------------------
# Location Check
# -------------------------------
def check_location(candidate_location, allowed_locations):

    if not allowed_locations:
        return True

    return candidate_location.lower() in [
        loc.lower()
        for loc in allowed_locations
    ]


# -------------------------------
# Availability Check
# -------------------------------
def check_availability(is_available, required):

    if not required:
        return True

    return is_available


# -------------------------------
# Main Engine
# -------------------------------
def evaluate_candidate(
    candidate,
    rules=DEFAULT_RULES
):

    ats_score = safe_value(
        candidate.get("final_score"),
        0
    )

    skills = safe_value(
        candidate.get("skills"),
        []
    )

    experience = safe_value(
        candidate.get("total_experience"),
        0
    )

    location = safe_value(
        candidate.get("location"),
        ""
    )

    available = safe_value(
        candidate.get("available"),
        True
    )

    skill_ok = check_mandatory_skills(
        skills,
        rules["mandatory_skills"]
    )

    exp_ok = check_experience(
        experience,
        rules["min_experience"],
        rules["max_experience"]
    )

    loc_ok = check_location(
        location,
        rules["allowed_locations"]
    )

    avail_ok = check_availability(
        available,
        rules["availability_required"]
    )

    if (
        ats_score >= rules["min_ats_score"]
        and skill_ok
        and exp_ok
        and loc_ok
        and avail_ok
    ):
        status = "Eligible"

    elif ats_score >= (
        rules["min_ats_score"] - 15
    ):
        status = "Review"

    else:
        status = "Rejected"

    return {
        "candidate_id": candidate.get(
            "candidate_id"
        ),
        "eligibility_status": status,
        "checks": {
            "ats_score": ats_score,
            "skill_match": skill_ok,
            "experience_match": exp_ok,
            "location_match": loc_ok,
            "availability_match": avail_ok
        }
    }


# -------------------------------
# Batch Evaluation
# -------------------------------
def evaluate_candidates_batch(
    candidates,
    rules
):

    results = []

    for candidate in candidates:

        result = evaluate_candidate(
            candidate,
            rules
        )

        results.append(result)

    return results