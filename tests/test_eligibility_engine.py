from screening_ai.eligibility_engine import (
    evaluate_candidate
)


def test_eligibility():

    candidate = {
        "final_score": 80,
        "skills": ["Python"],
        "total_experience": 3
    }

    rules = {
        "min_ats_score": 70,
        "mandatory_skills": ["Python"],
        "min_experience": 2,
        "max_experience": 5,
        "allowed_locations": [],
        "availability_required": False
    }

    result = evaluate_candidate(
        candidate,
        rules
    )

    assert (
        result["eligibility_status"]
        == "Eligible"
    )


print("All tests passed!")