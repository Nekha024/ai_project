"""
Transcript Cleanup Engine
"""

import re


def advanced_clean(text):

    text = text.lower()

    filler_words = [
        "um",
        "uh",
        "like",
        "you know"
    ]

    for word in filler_words:

        text = re.sub(
            rf"\b{word}\b",
            "",
            text
        )

    # Remove repeated words

    text = re.sub(
        r"\b(\w+)( \1\b)+",
        r"\1",
        text
    )

    # Remove punctuation

    text = re.sub(
        r"[^\w\s]",
        "",
        text
    )

    # Remove extra spaces

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()