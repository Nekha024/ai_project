from internal_review.review_report import (
    generate_review_report,
    get_system_flow
)


def test_review_report():

    report = generate_review_report()

    assert report["title"] == (
        "Zecpath AI Internal System Review Report"
    )

    assert report["system_status"] == (
        "Functionally complete and ready for controlled deployment"
    )


def test_system_walkthrough():

    flow = get_system_flow()

    assert "Resume Upload" in flow
    assert "ATS Scoring" in flow
    assert "Screening AI" in flow
    assert "HR Interview AI" in flow
    assert "Technical AI" in flow
    assert "Decision AI" in flow
    assert "Hiring Report" in flow


def test_accuracy_gaps():

    report = generate_review_report()

    assert len(report["accuracy_gaps"]) == 3


def test_ux_issues():

    report = generate_review_report()

    assert len(report["ux_issues"]) == 3


def test_performance_issues():

    report = generate_review_report()

    assert len(report["performance_issues"]) == 3


def test_current_state():

    report = generate_review_report()

    assert report["current_state"]["accuracy"] == "88%"
    assert report["current_state"]["latency"] == "2s"
    assert report["current_state"]["ux"] == "Moderate"


def test_target_state():

    report = generate_review_report()

    assert report["target_state"]["accuracy"] == "95%+"
    assert report["target_state"]["latency"] == "<1s"
    assert report["target_state"]["ux"] == "High"