import re

def normalize_transcript(text):

    text = text.lower()

    fillers = [
        "um",
        "uh",
        "like",
        "you know"
    ]

    for f in fillers:
        text = re.sub(
            rf"\b{f}\b",
            "",
            text
        )

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()