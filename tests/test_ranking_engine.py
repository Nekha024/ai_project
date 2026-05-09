from ats_engine.ranking_engine import (
    rank_candidates
)


def test_ranking():

    candidates = [

        {
            "candidate_id": "C1",
            "final_score": 50
        },

        {
            "candidate_id": "C2",
            "final_score": 80
        }
    ]

    ranked = rank_candidates(
        candidates
    )

    assert ranked[0][
        "candidate_id"
    ] == "C2"

    print(
        "✅ Ranking engine test passed!"
    )


test_ranking()