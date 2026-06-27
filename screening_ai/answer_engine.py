import re

# -------------------------------
# Intent Keywords Mapping
# -------------------------------

INTENT_MAP = {
    "introduction": ["introduce", "about myself", "background"],
    "experience": ["experience", "years", "worked", "role"],
    "skills": ["skills", "technologies", "tools"],
    "salary": ["salary", "ctc", "pay"],
    "availability": ["notice period", "available", "join"]
}

# -------------------------------
# Intent Classification
# -------------------------------

def classify_intent(text):
    text_lower = text.lower()

    for intent, keywords in INTENT_MAP.items():
        for keyword in keywords:
            if keyword in text_lower:
                return intent

    return "unknown"

# -------------------------------
# Skill Extraction
# -------------------------------

SKILL_DB = [
    "python",
    "java",
    "django",
    "react",
    "sql"
]

def extract_skills(text):
    text = text.lower()

    return [
        skill
        for skill in SKILL_DB
        if skill in text
    ]

# -------------------------------
# Experience Extraction
# -------------------------------

def extract_experience(text):

    match = re.search(
        r"(\d+)\s*(year|years)",
        text.lower()
    )

    if match:
        return int(match.group(1))

    return 0

# -------------------------------
# Salary Extraction
# -------------------------------

def extract_salary(text):

    match = re.search(
        r"(\d+)\s*(lpa|lakhs|k)",
        text.lower()
    )

    if match:
        return match.group(0)

    return None

# -------------------------------
# Availability Detection
# -------------------------------

def extract_availability(text):

    text = text.lower()

    if "immediate" in text:
        return "Immediate"

    if "notice" in text:
        return "Notice Period"

    return "Unknown"

# -------------------------------
# Off Topic Detection
# -------------------------------

def is_off_topic(intent):
    return intent == "unknown"

# -------------------------------
# Vague Answer Detection
# -------------------------------

def is_vague(text):

    vague_words = [
        "maybe",
        "not sure",
        "don't know"
    ]

    return any(
        word in text.lower()
        for word in vague_words
    )

# -------------------------------
# Missing Answer Detection
# -------------------------------

def detect_missing_answer(text):

    if not text:
        return True

    return len(text.strip()) < 3

# -------------------------------
# Main Processing Function
# -------------------------------

def process_answer(
    question_id,
    answer_text
):

    return {
        "question_id": question_id,
        "original_text": answer_text,
        "intent": classify_intent(answer_text),
        "skills": extract_skills(answer_text),
        "experience_years": extract_experience(answer_text),
        "salary": extract_salary(answer_text),
        "availability": extract_availability(answer_text),
        "off_topic": is_off_topic(
            classify_intent(answer_text)
        ),
        "is_vague": is_vague(answer_text),
        "is_missing": detect_missing_answer(answer_text)
    }