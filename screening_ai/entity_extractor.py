import re


SKILLS = [
    "python",
    "django",
    "java",
    "react",
    "sql",
    "javascript",
    "aws"
]


def extract_skills(text):

    found = []

    text = text.lower()

    for skill in SKILLS:

        if skill in text:
            found.append(skill)

    return found


def extract_experience(text):

    pattern = r'(\d+)\s+year'

    match = re.search(
        pattern,
        text.lower()
    )

    if match:
        return int(match.group(1))

    return None


def extract_salary(text):

    pattern = r'(\d+)\s*lpa'

    match = re.search(
        pattern,
        text.lower()
    )

    if match:
        return match.group(1) + " LPA"

    return None


def extract_availability(text):

    text = text.lower()

    if "immediately" in text:
        return "Immediate"

    if "15 days" in text:
        return "15 Days"

    if "30 days" in text:
        return "30 Days"

    return None