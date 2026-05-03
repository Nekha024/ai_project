import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ats_engine.skill_extractor import extract_skills_with_confidence


def test_skill_extraction():
    text = """
    Skilled in Python, JavaScript, ReactJS.
    Experience with MERN stack and machine learning.
    """

    skills = extract_skills_with_confidence(text)

    print("\nExtracted Skills:\n")
    for skill, score in skills.items():
        print(f"{skill}: {score}")

    assert "python" in skills
    assert "react" in skills
    assert "mongodb" in skills  # from MERN

    print("\n✔ Skill Extraction Test Passed")


if __name__ == "__main__":
    test_skill_extraction()