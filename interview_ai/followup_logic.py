def should_trigger_followup(answer):
    if not answer:
        return True

    if len(answer.split()) < 5:
        return True

    if "not sure" in answer.lower():
        return True

    return False


def generate_followup(question):
    return (
        f"Could you please elaborate on: {question}?"
    )