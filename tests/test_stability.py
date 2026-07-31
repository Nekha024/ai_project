from interview_ai.stable_hr_ai import stable_hr_evaluation
from interview_ai.refined_scoring import refined_score_pipeline
from screening_ai.optimized_cleaner import advanced_clean


def test_stability():

    result = stable_hr_evaluation(
        [50, 60, 90, 30]
    )

    assert result["stable_score"] > 0


def test_refined_scores():

    result = refined_score_pipeline(
        [50, 60],
        [80, 90]
    )

    assert len(result) == 2


def test_cleaner():

    cleaned = advanced_clean(
        "Um um I like Python!!!"
    )

    assert "um" not in cleaned