# -------------------------------
# Threshold Configuration
# -------------------------------

THRESHOLDS = {
    "shortlist": 75,
    "review": 50
}


# -------------------------------
# Sort Candidates by Score
# -------------------------------

def rank_candidates(candidates):

    ranked = sorted(
        candidates,
        key=lambda x: x.get(
            "final_score",
            0
        ),
        reverse=True
    )

    # Assign ranks
    for idx, candidate in enumerate(
        ranked,
        start=1
    ):

        candidate["rank"] = idx

    return ranked


# -------------------------------
# Candidate Classification
# -------------------------------

def classify_candidate(score):

    if score >= THRESHOLDS["shortlist"]:
        return "Shortlisted"

    elif score >= THRESHOLDS["review"]:
        return "Review"

    else:
        return "Rejected"


# -------------------------------
# Apply Shortlisting Logic
# -------------------------------

def apply_shortlisting(candidates):

    for candidate in candidates:

        score = candidate.get(
            "final_score",
            0
        )

        candidate["status"] = classify_candidate(
            score
        )

    return candidates


# -------------------------------
# Top Candidate Selector
# -------------------------------

def get_top_candidates(
    candidates,
    top_n=5
):

    return candidates[:top_n]


# -------------------------------
# Recruiter Summary
# -------------------------------

def generate_summary(candidates):

    shortlisted = sum(
        1 for c in candidates
        if c["status"] == "Shortlisted"
    )

    review = sum(
        1 for c in candidates
        if c["status"] == "Review"
    )

    rejected = sum(
        1 for c in candidates
        if c["status"] == "Rejected"
    )

    return {

        "total_candidates": len(candidates),

        "shortlisted": shortlisted,

        "review": review,

        "rejected": rejected
    }


# -------------------------------
# Complete Pipeline
# -------------------------------

def ranking_pipeline(
    candidates,
    job_id="J001"
):

    ranked = rank_candidates(
        candidates
    )

    shortlisted = apply_shortlisting(
        ranked
    )

    top_candidates = get_top_candidates(
        shortlisted
    )

    summary = generate_summary(
        shortlisted
    )

    return {

        "job_id": job_id,

        "summary": summary,

        "ranked_list": shortlisted,

        "top_candidates": top_candidates
    }