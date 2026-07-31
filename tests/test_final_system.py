from interview_ai.final_hr_module import run_hr_interview


def test_final_system():

    result = run_hr_interview(

        "C1",

        [],

        {
            "communication_score": 70
        },

        {

            "confidence": {
                "confidence_score": 70
            },

            "behavioral_score": 70,

            "contradiction": False

        }

    )

    assert "candidate_id" in result

    assert "final_score" in result

    assert "decision" in result