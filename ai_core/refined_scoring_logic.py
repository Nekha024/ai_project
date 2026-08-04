def consistency_adjustment(scores):
    values = list(scores.values())

    if not values:
        return 0

    variance = max(values) - min(values)

    if variance > 30:
        return -5

    elif variance < 10:
        return 5

    return 0


def refined_final_score(scores, base_score):
    adjustment = consistency_adjustment(scores)
    return max(min(base_score + adjustment, 100), 0)