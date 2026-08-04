from technical_ai.technical_pipeline import technical_pipeline


def test_technical():

    answer = """
    First I design architecture,
    then optimize because production
    applications need scalability.
    """

    result = technical_pipeline(

        answer,

        difficulty="advanced",

        is_correct=True

    )

    assert result["final_score"] > 0


if __name__ == "__main__":

    test_technical()

    print("Technical Skill Scoring Test Passed")