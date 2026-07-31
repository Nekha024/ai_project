def test_api_format():

    response = {

        "candidate_id": "C1",

        "final_score": 80

    }

    assert "candidate_id" in response

    assert "final_score" in response