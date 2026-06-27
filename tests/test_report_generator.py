from screening_ai.report_generator import (
    generate_screening_report
)

def test_report():

    report = generate_screening_report(
        "C1",
        "J1",
        [],
        [],
        []
    )

    assert "candidate_id" in report
    assert "decision" in report
    assert "summary" in report


if __name__ == "__main__":
    test_report()
    print("Report Generator Test Passed")