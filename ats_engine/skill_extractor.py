import re
from collections import defaultdict
from ats_engine.skills_dictionary import TECH_SKILLS, BUSINESS_SKILLS, CREATIVE_SKILLS, SKILL_STACKS


def normalize_text(text):
    return text.lower()


def extract_skills(text):
    text = normalize_text(text)

    extracted = defaultdict(float)

    # Combine all skill dictionaries
    all_skills = {**TECH_SKILLS, **BUSINESS_SKILLS, **CREATIVE_SKILLS}

    # 1. Direct skill match
    for skill, variants in all_skills.items():
        for v in variants:
            if re.search(rf"\b{re.escape(v)}\b", text):
                extracted[skill] += 1.0

    # 2. Skill stack detection
    for stack, skills in SKILL_STACKS.items():
        if stack in text:
            for s in skills:
                extracted[s] += 0.8  # slightly lower confidence

    return dict(extracted)


#Confidence Scoring Logic

def normalize_scores(skills_dict):
    max_score = max(skills_dict.values()) if skills_dict else 1

    return {
        skill: round(score / max_score, 2)
        for skill, score in skills_dict.items()
    }

# ✅ MAIN FUNCTION
def extract_skills_with_confidence(text):
    raw_skills = extract_skills(text)
    return normalize_scores(raw_skills)