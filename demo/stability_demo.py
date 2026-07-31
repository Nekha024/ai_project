from interview_ai.stable_hr_ai import stable_hr_evaluation
from interview_ai.refined_scoring import refined_score_pipeline
from screening_ai.optimized_cleaner import advanced_clean


def run_demo():

    print("\n===== Stable HR Evaluation =====")

    hr = stable_hr_evaluation(
        [50, 60, 90, 30]
    )

    print(hr)

    print("\n===== Refined Scores =====")

    scores = refined_score_pipeline(
        [50, 60, 90, 30],
        [70, 80, 90, 65]
    )

    print(scores)

    print("\n===== Transcript Cleaning =====")

    text = "Um um I like like Python!!!"

    print(advanced_clean(text))


if __name__ == "__main__":
    run_demo()