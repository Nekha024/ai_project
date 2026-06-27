import re


def clean_noise(text):

    # Remove background noise tags

    text = re.sub(
        r"\[.*?\]",
        "",
        text
    )

    # Remove excessive repeated characters

    text = re.sub(
        r"(.)\1{2,}",
        r"\1",
        text
    )

    return text.strip()


def detect_language_mix(text):

    local_words = [
        "hai",
        "enna",
        "chetta",
        "bhai"
    ]

    for word in local_words:

        if word in text.lower():
            return True

    return False