# -------------------------------
# Scoring Parameters Weightage
# -------------------------------

WEIGHTS = {
    "clarity": 0.25,
    "relevance": 0.30,
    "completeness": 0.25,
    "consistency": 0.20
}

# -------------------------------
# Clarity Score
# -------------------------------

def score_clarity(answer):
    word_count = len(answer.split())

    if word_count >= 15:
        return 100
    elif word_count >= 8:
        return 75
    elif word_count >= 3:
        return 50
    return 20

# -------------------------------
# Relevance Score
# -------------------------------

def score_relevance(structured_answer):
    if structured_answer["off_topic"]:
        return 20

    if structured_answer["intent"] != "unknown":
        return 100

    return 50

# -------------------------------
# Completeness Score
# -------------------------------

def score_completeness(structured_answer):
    score = 0

    if structured_answer["skills"]:
        score += 25

    if structured_answer["experience_years"] > 0:
        score += 25

    if structured_answer["salary"]:
        score += 25

    if structured_answer["availability"] != "Unknown":
        score += 25

    return score

# -------------------------------
# Consistency Score
# -------------------------------

def score_consistency(structured_answer):
    if structured_answer["is_vague"]:
        return 40

    return 100

# -------------------------------
# Normalize Final Score
# -------------------------------

def calculate_final_score(
    clarity,
    relevance,
    completeness,
    consistency
):
    final_score = (
        clarity * WEIGHTS["clarity"] +
        relevance * WEIGHTS["relevance"] +
        completeness * WEIGHTS["completeness"] +
        consistency * WEIGHTS["consistency"]
    )

    return round(final_score, 2)

# -------------------------------
# Main Question Scoring
# -------------------------------

def score_answer(structured_answer):

    clarity = score_clarity(
        structured_answer["original_text"]
    )

    relevance = score_relevance(
        structured_answer
    )

    completeness = score_completeness(
        structured_answer
    )

    consistency = score_consistency(
        structured_answer
    )

    final_score = calculate_final_score(
        clarity,
        relevance,
        completeness,
        consistency
    )

    return {
        "question_id": structured_answer["question_id"],
        "clarity": clarity,
        "relevance": relevance,
        "completeness": completeness,
        "consistency": consistency,
        "final_score": final_score
    }