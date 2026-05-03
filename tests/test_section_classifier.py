import sys
import os
from datetime import datetime

# FIX: add root path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from parsers.section_classifier import segment_resume


def test_section_detection():
    report = []
    status = "PASS"

    try:
        text = "SKILLS\nPython\nEXPERIENCE\nWorked at ABC"
        result = segment_resume(text)

        assert "skills" in result
        report.append("✔ Skills section detected")

        assert "experience" in result
        report.append("✔ Experience section detected")

    except AssertionError:
        status = "FAIL"
        report.append("❌ Assertion failed")

    except Exception as e:
        status = "ERROR"
        report.append(f"❌ Error: {str(e)}")

    # Save report
    os.makedirs("data/outputs", exist_ok=True)
    filename = "data/outputs/test_report.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write("=== TEST REPORT ===\n")
        f.write(f"Date: {datetime.now()}\n")
        f.write(f"Status: {status}\n\n")
        for line in report:
            f.write(line + "\n")

    print(f"📄 Report saved: {filename}")
    print(f"STATUS: {status}")


if __name__ == "__main__":
    test_section_detection()