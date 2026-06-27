from screening_ai.scoring_engine import score_answer

def score_questions(structured_answers):

    results = []

    for answer in structured_answers:
        results.append(score_answer(answer))

    return results