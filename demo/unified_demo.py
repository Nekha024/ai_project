from ai_core.unified_pipeline import unified_scoring_pipeline


def run_demo():

    report = unified_scoring_pipeline(

        candidate_id="C101",

        ats_score=82,

        screening_score=76,

        hr_score=88,

        candidate_type="technical"

    )

    print(report)


if __name__ == "__main__":
    run_demo()