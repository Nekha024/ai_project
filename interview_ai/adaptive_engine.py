def adapt_question_level(
    answer_quality,
    confidence_score
):

    if answer_quality in [
        "empty",
        "too_short"
    ]:
        return "simplify"

    if answer_quality == "basic":
        return "example"

    if (
        answer_quality == "good"
        and confidence_score > 0.7
    ):
        return "advanced"

    return "normal"


def generate_adaptive_question(
    base_question,
    mode
):

    if mode == "simplify":
        return (
            f"Let me simplify the question: "
            f"{base_question}"
        )

    if mode == "example":
        return (
            f"Can you give a real-world example for: "
            f"{base_question}?"
        )

    if mode == "advanced":
        return (
            f"Can you handle a complex scenario related to: "
            f"{base_question}?"
        )

    return base_question