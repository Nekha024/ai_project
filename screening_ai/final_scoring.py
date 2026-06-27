def calculate_screening_score(question_scores):

    if not question_scores:
        return 0

    total = sum(
        score["final_score"]
        for score in question_scores
    )

    return round(
        total / len(question_scores),
        2
    )