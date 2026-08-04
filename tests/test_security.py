from security.access_control import has_access
from security.audit_log import log_event


def test_access():

    assert has_access("admin", "delete") is True
    assert has_access("viewer", "write") is False


def test_audit():

    log = log_event("score", "C1", {"score": 80})

    assert log["candidate_id"] == "C1"
    assert log["event_type"] == "score"