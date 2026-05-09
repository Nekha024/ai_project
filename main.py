import json
from scoring.score import calculate_final_score
from parsers.resume_reader import extract_resume_text
from parsers.section_classifier import segment_resume

from ats_engine.semantic_matcher import (
    match_resume_to_jd,
    classify_match
)


def load_json(path):
    with open(path, "r") as f:
        return json.load(f)


def save_text(text):
    with open("data/cleaned_resume.txt", "w") as f:
        f.write(text)


def main():

    # 🔹 Step 1: Extract text from resume
    file_path = "data/resumes/sample.pdf"
    text = extract_resume_text(file_path)

    print("Extracted Text Preview:\n")
    print(text[:300])

    save_text(text)

    # 🔹 Step 1.1: DAY 8 - SECTION SEGMENTATION
    sections = segment_resume(text)

    # Save structured output
    output_path = "data/outputs/output.json"

    with open(output_path, "w") as f:
        json.dump(sections, f, indent=4)

    print("\nStructured Sections saved at:", output_path)
    print(json.dumps(sections, indent=2)[:500])

    # 🔹 Step 2: Load structured data
    candidate = load_json("data/resume.json")
    job = load_json("data/job.json")

    # 🔹 Step 3: Calculate keyword-based score
    score = calculate_final_score(candidate, job)

    print(f"\nFinal Candidate Score: {score}%")

    # 🔹 Step 4: Semantic Matching (ADD HERE)
    semantic_result = match_resume_to_jd(
        candidate,
        job
    )

    print("\nSemantic Matching Result:\n")
    print(json.dumps(semantic_result, indent=2))

    match_type = classify_match(
        semantic_result["final_similarity_score"]
    )

    print("\nMatch Type:", match_type)


if __name__ == "__main__":
    main()