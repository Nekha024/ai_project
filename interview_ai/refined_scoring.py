"""
Bias Reduction and Score Refinement
"""


def normalize_scores(scores):

    if not scores:
        return []

    minimum = min(scores)
    maximum = max(scores)

    if minimum == maximum:
        return scores

    normalized = []

    for score in scores:

        normalized.append(

            round(
                ((score - minimum) /
                 (maximum - minimum)) * 100,
                2
            )

        )

    return normalized


def reduce_bias(score, confidence):

    adjusted = (score * 0.90) + (confidence * 0.10)

    return round(adjusted, 2)


def refined_score_pipeline(
        scores,
        confidence_scores):

    normalized = normalize_scores(scores)

    final_scores = []

    for score, confidence in zip(
            normalized,
            confidence_scores):

        final_scores.append(

            reduce_bias(
                score,
                confidence
            )

        )

    return final_scores