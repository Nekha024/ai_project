from collections import Counter


def calculate_accuracy(results):

    matched = sum(

        1

        for item in results

        if item["decision_ai"] == item["decision_human"]

    )

    return round(

        matched / len(results) * 100,

        2

    )


def candidate_distribution(results):

    return Counter(

        item["candidate_type"]

        for item in results

    )


def average_scores(results):

    ai = sum(

        x["ai_score"]

        for x in results

    ) / len(results)

    human = sum(

        x["human_score"]

        for x in results

    ) / len(results)

    return {

        "average_ai_score": round(ai, 2),

        "average_human_score": round(human, 2)

    }