#Create Experience Parser

import re
from datetime import datetime

# Month mapping
MONTHS = {
    "jan": 1, "feb": 2, "mar": 3, "apr": 4,
    "may": 5, "jun": 6, "jul": 7, "aug": 8,
    "sep": 9, "oct": 10, "nov": 11, "dec": 12
}


def parse_date(text):
    text = text.lower()

    if "present" in text:
        return datetime.now()

    for m in MONTHS:
        if m in text:
            year = int(re.findall(r"\d{4}", text)[0])
            return datetime(year, MONTHS[m], 1)

    # fallback (year only)
    year = int(re.findall(r"\d{4}", text)[0])
    return datetime(year, 1, 1)


def extract_experience(text):
    experiences = []

    # Simple pattern (can improve later)
    pattern = r"(?P<title>.+?) at (?P<company>.+?)\n(?P<start>.+?) - (?P<end>.+)"

    matches = re.finditer(pattern, text, re.IGNORECASE)

    for match in matches:
        title = match.group("title").strip()
        company = match.group("company").strip()
        start = parse_date(match.group("start"))
        end = parse_date(match.group("end"))

        duration_months = (end.year - start.year) * 12 + (end.month - start.month)

        experiences.append({
            "title": title,
            "company": company,
            "start": start,
            "end": end,
            "duration_months": duration_months
        })

    return experiences

#Total Experience Calculation

def calculate_total_experience(experiences):
    total_months = sum(exp["duration_months"] for exp in experiences)
    return round(total_months / 12, 2)  # years

#Gap & Overlap Detection

def detect_gaps_and_overlaps(experiences):
    experiences = sorted(experiences, key=lambda x: x["start"])

    gaps = []
    overlaps = []

    for i in range(len(experiences) - 1):
        current = experiences[i]
        next_exp = experiences[i + 1]

        if current["end"] < next_exp["start"]:
            gap = (next_exp["start"] - current["end"]).days // 30
            gaps.append(gap)

        if current["end"] > next_exp["start"]:
            overlap = (current["end"] - next_exp["start"]).days // 30
            overlaps.append(overlap)

    return gaps, overlaps

#Structured Output
def build_experience_profile(text, job_description):
    experiences = extract_experience(text)

    total_exp = calculate_total_experience(experiences)
    gaps, overlaps = detect_gaps_and_overlaps(experiences)

    from scoring.relevance import compute_experience_relevance
    relevance = compute_experience_relevance(experiences, job_description)

    return {
        "experiences": experiences,
        "total_experience_years": total_exp,
        "gaps_months": gaps,
        "overlaps_months": overlaps,
        "relevance_score": relevance
    }