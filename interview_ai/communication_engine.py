import re

# -------------------------------
# Filler Words
# -------------------------------

FILLER_WORDS = [
    "um",
    "uh",
    "like",
    "you know",
    "actually",
    "basically"
]


# -------------------------------
# Fluency Score
# -------------------------------

def score_fluency(text):

    sentences = re.split(r"[.!?]", text)

    valid = [
        s for s in sentences
        if len(s.split()) > 3
    ]

    if len(valid) >= 2:
        return 1.0

    elif len(valid) == 1:
        return 0.6

    return 0.3


# -------------------------------
# Grammar Score
# -------------------------------

def score_grammar(text):

    if (
        text
        and text[0].isupper()
        and text.strip().endswith(
            (".", "!", "?")
        )
    ):
        return 1.0

    elif len(text.split()) > 5:
        return 0.7

    return 0.4


# -------------------------------
# Vocabulary Score
# -------------------------------

def score_vocabulary(text):

    words = text.lower().split()

    unique = set(words)

    ratio = len(unique) / (len(words) + 1)

    if ratio > 0.6:
        return 1.0

    elif len(unique) > 5:
        return 0.7

    return 0.4


# -------------------------------
# Clarity Score
# -------------------------------

def score_clarity(text):

    length = len(text.split())

    if length > 12:
        return 1.0

    elif length > 6:
        return 0.7

    return 0.4


# -------------------------------
# Structure Score
# -------------------------------

def score_structure(text):

    text = text.lower()

    if (
        "because" in text
        or "for example" in text
    ):
        return 1.0

    elif len(text.split()) > 6:
        return 0.7

    return 0.4


# -------------------------------
# Filler Penalty
# -------------------------------

def filler_penalty(text):

    text = text.lower()

    count = sum(
        text.count(word)
        for word in FILLER_WORDS
    )

    return min(count * 0.1, 0.5)


# -------------------------------
# Final Communication Score
# -------------------------------

def calculate_communication_score(text):

    fluency = score_fluency(text)
    grammar = score_grammar(text)
    vocabulary = score_vocabulary(text)
    clarity = score_clarity(text)
    structure = score_structure(text)

    penalty = filler_penalty(text)

    score = (
        fluency * 0.2
        + grammar * 0.2
        + vocabulary * 0.2
        + clarity * 0.2
        + structure * 0.2
    )

    score = max(score - penalty, 0)

    return {
        "communication_score": round(score * 100, 2),
        "breakdown": {
            "fluency": round(fluency, 2),
            "grammar": round(grammar, 2),
            "vocabulary": round(vocabulary, 2),
            "clarity": round(clarity, 2),
            "structure": round(structure, 2),
            "penalty": round(penalty, 2)
        }
    }