import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ats_engine.experience_parser import build_experience_profile


def test_experience():
    text = """
    Software Engineer at ABC Corp
    Jan 2020 - Dec 2022

    Data Analyst at XYZ Ltd
    Jan 2023 - Present
    """

    job_desc = "Looking for Python, SQL, data analysis skills"

    result = build_experience_profile(text, job_desc)

    print("\nExperience Profile:\n", result)

    assert result["total_experience_years"] > 0

    print("\n✔ Test Passed")


if __name__ == "__main__":
    test_experience()