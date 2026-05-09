import re
import json
import spacy
from collections import defaultdict

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# -------------------------------
# 1. SECTION KEYWORDS
# -------------------------------
SECTION_KEYWORDS = {
    "skills": [
        "skills",
        "technical skills",
        "core competencies"
    ],

    "experience": [
        "experience",
        "work experience",
        "professional experience",
        "employment history"
    ],

    "education": [
        "education",
        "academic background",
        "qualifications"
    ],

    "projects": [
        "projects"
    ],

    "certifications": [
        "certifications",
        "licenses"
    ],

    "summary": [
        "summary",
        "profile summary",
        "objective"
    ]
}

# -------------------------------
# 2. SAMPLE RESUME TEXT
# -------------------------------
SAMPLE_RESUME = """
John Doe
Email: john.doe@email.com

Education
B.Tech in Computer Science, XYZ University, 2022

Skills
Python, Java, SQL, Machine Learning

Experience
Software Intern at ABC Company
Developed web applications using Python

Projects
Built a resume parser using NLP
Created a chatbot using machine learning

Certifications
Certified Python Developer
"""

# -------------------------------
# 3. CLEAN TEXT
# -------------------------------
def clean_line(line):
    line = line.strip()
    line = re.sub(r'\s+', ' ', line)
    return line


# -------------------------------
# 4. RULE-BASED HEADING DETECTION
# -------------------------------
def detect_heading(line):
    line_lower = line.lower()

    for section, keywords in SECTION_KEYWORDS.items():
        for kw in keywords:
            if kw in line_lower:
                return section
    return None


# -------------------------------
# 5. NLP-BASED CLASSIFICATION
# -------------------------------
def classify_line_nlp(line):
    text = line.lower()

    if any(word in text for word in ["python", "java", "sql", "machine learning"]):
        return "skills"

    if any(word in text for word in ["university", "b.tech", "degree", "school"]):
        return "education"

    if any(word in text for word in ["developed", "worked", "intern", "company"]):
        return "experience"

    if any(word in text for word in ["project", "built", "created"]):
        return "projects"

    if any(word in text for word in ["certified", "certificate"]):
        return "certifications"

    return "unknown"


# -------------------------------
# 6. SEGMENT RESUME (SMART)
# -------------------------------
def segment_resume(text):

    sections = defaultdict(list)

    lines = re.split(
    r'(?=\b(?:skills|technical skills|experience|professional experience|education|projects|certifications|summary|profile summary)\b)',
    text,
    flags=re.IGNORECASE
)

    for raw_line in lines:

        line = clean_line(raw_line)

        if not line:
            continue

        # Step 1: Try heading detection
        detected = detect_heading(line)

        if detected:
            sections[detected].append(line)
            continue

        # Step 2: NLP classification
        predicted = classify_line_nlp(line)

        # Step 3: Store directly in predicted section
        if predicted != "unknown":
            sections[predicted].append(line)

        else:
            sections["other"].append(line)

    return dict(sections)


# -------------------------------
# 7. SAVE JSON
# -------------------------------
def save_to_json(data, filename="data/outputs/output.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


# -------------------------------
# 8. MAIN
# -------------------------------
def process_resume_text(text):
    print("🧠 Segmenting intelligently...")
    sections = segment_resume(text)

    print("💾 Saving JSON...")
    save_to_json(sections)

    print("✅ Done!")


# -------------------------------
# 9. RUN
# -------------------------------
if __name__ == "__main__":
    process_resume_text(SAMPLE_RESUME)