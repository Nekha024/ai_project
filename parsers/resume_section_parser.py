import fitz  # PyMuPDF
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
    "skills": ["skills", "technical skills", "core competencies"],
    "experience": ["experience", "work experience", "professional experience", "employment history"],
    "education": ["education", "academic background", "qualifications"],
    "projects": ["projects"],
    "certifications": ["certifications", "licenses"]
}

# -------------------------------
# 2. EXTRACT TEXT FROM PDF
# -------------------------------
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


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
            if kw == line_lower:
                return section
    return None


# -------------------------------
# 5. NLP-BASED CLASSIFICATION
# -------------------------------
def classify_line_nlp(line):
    """
    Classify content when heading is missing
    """
    doc = nlp(line)

    text = line.lower()

    # Simple NLP + keyword hybrid
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
    current_section = "unknown"

    lines = text.split("\n")

    for raw_line in lines:
        line = clean_line(raw_line)

        if not line:
            continue

        # Step 1: Try heading detection
        detected = detect_heading(line)

        if detected:
            current_section = detected
            continue

        # Step 2: If no heading, classify content
        predicted = classify_line_nlp(line)

        if current_section == "unknown":
            current_section = predicted

        sections[current_section].append(line)

    return dict(sections)


# -------------------------------
# 7. SAVE JSON
# -------------------------------
def save_to_json(data, filename="data/resumes/nlp_resume.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


# -------------------------------
# 8. MAIN
# -------------------------------
def process_resume(pdf_path):
    print("📄 Extracting text...")
    text = extract_text_from_pdf(pdf_path)

    print("🧠 Segmenting intelligently...")
    sections = segment_resume(text)

    print("💾 Saving JSON...")
    save_to_json(sections)

    print("✅ Done!")


# -------------------------------
# 9. RUN
# -------------------------------
if __name__ == "__main__":
    pdf_file = "data/resumes/resume.pdf" 
    process_resume(pdf_file)