from screening_ai.report_generators import (
    generate_screening_report
)

def test_system():

    report = generate_screening_report(
        "C1",
        "J1",
        [],
        [],
        []
    )

    assert "candidate_id" in report
    assert "decision" in report

if __name__ == "__main__":
    test_system()
    print("System test passed")