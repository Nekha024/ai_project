def explain_score(score_data):

    return {
        "question_id": score_data["question_id"],
        "score": score_data["final_score"],
        "explanation": {
            "clarity":
                f"Clarity Score = {score_data['clarity']}",
            "relevance":
                f"Relevance Score = {score_data['relevance']}",
            "completeness":
                f"Completeness Score = {score_data['completeness']}",
            "consistency":
                f"Consistency Score = {score_data['consistency']}"
        }
    }