from demo.full_pipeline_simulation import run_demo_pipeline


def test_strong_candidate():
    result = run_demo_pipeline("C001")

    assert result["candidate_id"] == "C001"
    assert result["result"]["final_score"] == 85
    assert result["result"]["decision"] == "Selected"


def test_average_candidate():
    result = run_demo_pipeline("C002")

    assert result["candidate_id"] == "C002"
    assert result["result"]["final_score"] == 68
    assert result["result"]["decision"] == "Hold / Review"


def test_weak_candidate():
    result = run_demo_pipeline("C003")

    assert result["candidate_id"] == "C003"
    assert result["result"]["final_score"] == 45
    assert result["result"]["decision"] == "Rejected"


def test_unknown_candidate():
    result = run_demo_pipeline("C999")

    assert result["candidate_id"] == "C999"
    assert result["result"] is None