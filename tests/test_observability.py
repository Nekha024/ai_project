from observability.logging import log_event


def test_log_event():
    log = log_event(
        "ATS",
        "test",
        {
            "candidate_id": "C101",
            "score": 78
        }
    )

    assert "service" in log
    assert log["service"] == "ATS"
    assert log["event_type"] == "test"
    assert "timestamp" in log