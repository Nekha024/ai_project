from ai_core.performance_optimized import (
    cached_ats_score,
    batch_resume_processing
)


def test_cached_ats():
    result = cached_ats_score("candidate_profile_1")

    assert 0 <= result <= 99


def test_batch_processing():
    resumes = [1, 2, 3, 4]

    result = batch_resume_processing(
        resumes,
        lambda x: x * 2
    )

    assert result == [2, 4, 6, 8]