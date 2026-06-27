import re

# -------------------------------
# Intent Mapping
# -------------------------------

INTENT_MAP = {
    "introduction": ["introduce", "about myself", "background"],
    "experience": ["experience", "years", "worked", "role"],
    "skills": ["skills", "technologies", "tools"],
    "salary": ["salary", "ctc", "pay"],
    "availability": ["notice period", "available", "join"]
}

# -------------------------------
# Intent Classifier
# -------------------------------

def classify_intent(text):
    text = text.lower()

    for intent, keywords in INTENT_MAP.items():
        for kw in keywords:
            if kw in text:
                return intent

    return "unknown"

# -------------------------------
# Extract Skills
# -------------------------------

SKILL_DB = ["python", "java", "django", "react", "sql"]

def extract_skills(text):
    text = text.lower()
    return [s for s in SKILL_DB if s in text]

# -------------------------------
# Extract Experience
# -------------------------------

def extract_experience(text):
    match = re.search(r"(\d+)\s*(year|years)", text.lower())
    return int(match.group(1)) if match else 0

# -------------------------------
# Salary Extraction
# -------------------------------

def extract_salary(text):
    match = re.search(r"(\d+)\s*(lpa|lakhs|k)", text.lower())
    return match.group(0) if match else None

# -------------------------------
# Availability
# -------------------------------

def extract_availability(text):
    text = text.lower()

    if "immediate" in text:
        return "Immediate"
    if "notice" in text:
        return "Notice Period"

    return "Unknown"

# -------------------------------
# Helpers
# -------------------------------

def is_vague(text):
    vague_words = ["maybe", "not sure", "don't know"]
    return any(w in text.lower() for w in vague_words)


def detect_missing_answer(text):
    return not text or len(text.strip()) < 3


# -------------------------------
# MAIN FUNCTION (IMPORTANT)
# -------------------------------

def process_answer(question_id, answer_text):

    intent = classify_intent(answer_text)

    return {
        "question_id": question_id,
        "original_text": answer_text,
        "intent": intent,
        "skills": extract_skills(answer_text),
        "experience_years": extract_experience(answer_text),
        "salary": extract_salary(answer_text),
        "availability": extract_availability(answer_text),
        "off_topic": (intent == "unknown"),
        "is_vague": is_vague(answer_text),
        "is_missing": detect_missing_answer(answer_text)
    }