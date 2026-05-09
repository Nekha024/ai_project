#Create Education & Certification Parser

import re
from collections import defaultdict


# -------------------------------
# 1. NORMALIZATION MAPS
# -------------------------------
DEGREE_MAP = {
    "b.tech": "bachelor",
    "bachelor": "bachelor",
    "m.tech": "master",
    "master": "master",
    "phd": "phd"
}

FIELDS = ["computer science", "information technology", "business", "marketing"]

CERT_CATEGORIES = {
    "aws": "cloud",
    "azure": "cloud",
    "google cloud": "cloud",
    "python": "programming",
    "data science": "data",
    "machine learning": "data"
}


# -------------------------------
# 2. EDUCATION EXTRACTION
# -------------------------------
def extract_education(text):
    education_list = []

    lines = [line.strip() for line in text.split("\n") if line.strip()]

    for i in range(len(lines)):
        line = lines[i].lower()

        # detect degree line
        if any(deg in line for deg in ["b.tech", "m.tech", "bachelor", "master", "phd"]):

            degree_raw = next(
                (deg for deg in ["b.tech", "m.tech", "bachelor", "master", "phd"] if deg in line),
                "unknown"
            )

            degree = DEGREE_MAP.get(degree_raw, degree_raw)

            # next line = institution (if exists)
            institution = lines[i + 1] if i + 1 < len(lines) else "unknown"

            # next next line = year (if exists)
            year = "unknown"
            if i + 2 < len(lines):
                match = re.search(r"\d{4}", lines[i + 2])
                if match:
                    year = match.group()

            # detect field
            field = "unknown"
            for f in FIELDS:
                if f in line:
                    field = f
                    break

            education_list.append({
                "degree": degree,
                "field": field,
                "institution": institution,
                "graduation_year": year
            })

    return education_list


#Certification Extraction

# -------------------------------
# 3. CERTIFICATION EXTRACTION
# -------------------------------
def extract_certifications(text):
    certifications = []

    lines = text.split("\n")

    for line in lines:
        line_lower = line.lower()

        if "certified" in line_lower or "certificate" in line_lower:
            category = "general"

            for key, value in CERT_CATEGORIES.items():
                if key in line_lower:
                    category = value
                    break

            certifications.append({
                "name": line.strip(),
                "category": category
            })

    return certifications


#Combine into Final Profile

def build_academic_profile(text, job_description):
    education = extract_education(text)
    certifications = extract_certifications(text)

    from scoring.education_relevance import compute_education_relevance
    relevance = compute_education_relevance(education, job_description)

    return {
        "education": education,
        "certifications": certifications,
        "education_relevance_score": relevance
    }