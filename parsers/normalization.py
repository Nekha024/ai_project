import re


# -------------------------------
# Standard Resume Normalization
# -------------------------------

def normalize_resume_text(text):

    text = text.lower()

    # Remove special characters
    text = re.sub(
        r"[^a-z0-9\s\.\,\-]",
        "",
        text
    )

    # Normalize spaces
    text = re.sub(
        r"\s+",
        " ",
        text
    )

    # Standardize headings
    replacements = {

        "professional experience":
        "experience",

        "work experience":
        "experience",

        "academic background":
        "education",

        "skill set":
        "skills"
    }

    for key, value in replacements.items():

        text = text.replace(
            key,
            value
        )

    return text.strip()