from ats_engine.fairness_engine import (
    normalize_scores,
    mask_sensitive_data,
    generate_fair_score
)


def test_fairness_engine():

    candidates = [

        {
            "candidate_id": "C1",
            "final_score": 90,
            "skill_score": 85,
            "semantic_score": 88,
            "name": "John"
        },

        {
            "candidate_id": "C2",
            "final_score": 70,
            "skill_score": 65,
            "semantic_score": 75,
            "name": "Alice"
        }
    ]

    candidates = normalize_scores(
        candidates
    )

    for c in candidates:

        mask_sensitive_data(c)

        generate_fair_score(c)

    print(
        "✅ Fairness engine test passed!"
    )

    print(candidates)


test_fairness_engine()