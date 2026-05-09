import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from parsers.education_parser import build_academic_profile


def test_education():
    text = """
    B.Tech in Computer Science
    XYZ University
    2022

    Certified Python Developer
    AWS Certified Solutions Architect
    """

    job_desc = "Looking for computer science background and cloud skills"

    result = build_academic_profile(text, job_desc)

    print("\nAcademic Profile:\n", result)

    assert len(result["education"]) > 0
    assert len(result["certifications"]) > 0

    print("\n✔ Test Passed")


if __name__ == "__main__":
    test_education()