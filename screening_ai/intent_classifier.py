import re

INTENT_PATTERNS = {
    "self_introduction": [
        "i am",
        "my name is",
        "i'm"
    ],

    "experience_info": [
        "years experience",
        "worked",
        "experience"
    ],

    "skill_info": [
        "python",
        "java",
        "django",
        "react",
        "sql"
    ],

    "availability_info": [
        "immediately",
        "notice period",
        "available"
    ],

    "salary_expectation": [
        "salary",
        "ctc",
        "expected salary",
        "lpa"
    ]
}


def classify_intent(text):

    text = text.lower()

    for intent, keywords in INTENT_PATTERNS.items():

        for keyword in keywords:

            if keyword in text:
                return intent

    return "unknown"