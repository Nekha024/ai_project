from screening_ai.improved_intent import (
    improved_intent_classification,
    get_decision
)


def simulate_test():

    answer = (
        "I have 2 years experience "
        "working as a Python developer"
    )

    intent = improved_intent_classification(
        answer
    )

    score = 68

    result = {
        "answer": answer,
        "intent": intent,
        "score": score,
        "decision": get_decision(score)
    }

    return result


if __name__ == "__main__":
    print(simulate_test())