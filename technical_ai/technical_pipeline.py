from technical_ai.technical_scoring_engine import (
    calculate_technical_score,
    classify_answer_depth
)

from technical_ai.difficulty_normalizer import normalize_difficulty


def technical_pipeline(answer,
                       difficulty="basic",
                       is_correct=True):

    base = calculate_technical_score(answer,is_correct)

    normalized = normalize_difficulty(
        base["technical_score"],
        difficulty
    )

    return {

        "final_score":normalized,

        "depth":classify_answer_depth(answer),

        "details":base

    }


if __name__ == "__main__":

    ans = """
    First I design the architecture,
    then optimize database queries because
    production applications require scalability.
    """

    print(
        technical_pipeline(
            ans,
            "advanced",
            True
        )
    )