import json

from scoring.score import calculate_final_score
from parsers.resume_reader import extract_resume_text
from parsers.section_classifier import segment_resume

from ats_engine.semantic_matcher import (
    match_resume_to_jd,
    classify_match
)

from ats_engine.ats_scorer import (
    generate_candidate_score
)

from ats_engine.ranking_engine import (
    ranking_pipeline
)

from ats_engine.fairness_engine import (
    normalize_scores,
    mask_sensitive_data,
    generate_fair_score
)

from parsers.normalization import (
    normalize_resume_text
)


from screening_ai.eligibility_engine import (
    evaluate_candidate
)

# -------------------------------
# Load JSON
# -------------------------------

def load_json(path):

    with open(path, "r") as f:
        return json.load(f)


# -------------------------------
# Save Cleaned Text
# -------------------------------

def save_text(text):

    with open("data/cleaned_resume.txt", "w") as f:
        f.write(text)


# -------------------------------
# MAIN
# -------------------------------

def main():

    # 🔹 Step 1: Extract text from resume

    file_path = "data/resumes/sample.pdf"

    text = extract_resume_text(file_path)

    print("\n" + "="*50)
    print("STEP 1: EXTRACTING TEXT FROM RESUME")
    print("="*50)
    print("\nExtracted Text Preview:\n")

    print(text[:300])

    save_text(text)

    # 🔹 Step 1.1: Resume Section Segmentation

    sections = segment_resume(text)

    output_path = "data/outputs/output.json"

    with open(output_path, "w") as f:
        json.dump(sections, f, indent=4)

    print("\n" + "="*50)
    print("STEP 2: STRUCTURING RESUME DATA")
    print("="*50)
    print(f"\nStructured Sections saved at: {output_path}")

    print(json.dumps(sections, indent=2)[:500])

    # 🔹 Step 2: Load structured data

    candidate = load_json("data/resume.json")

    job = load_json("data/job.json")

    # 🔹 Step 3: Keyword-Based ATS Score

    score = calculate_final_score(
        candidate,
        job
    )

    print("\n" + "="*50)
    print("STEP 3: CALCULATING KEYWORD ATS SCORE")
    print("="*50)
    print(f"\nFinal Keyword Score: {score}%")

    # 🔹 Step 4: Semantic Matching

    semantic_result = match_resume_to_jd(
        candidate,
        job
    )

    print("\n" + "="*50)
    print("STEP 4: AI SEMANTIC MATCHING")
    print("="*50)
    print("\nSemantic Matching Result:\n")

    print(
        json.dumps(
            semantic_result,
            indent=2
        )
    )

    match_type = classify_match(
        semantic_result["final_similarity_score"]
    )

    print("\nMatch Type:", match_type)

    # 🔹 Step 5: ATS Scoring Engine

    candidate_scores = {

        "candidate_id": "C123",

        "skill_score": 80,

        "experience_score": 75,

        "education_score": 70,

        "semantic_score":
        semantic_result[
            "final_similarity_score"
        ]
    }

    ats_result = generate_candidate_score(
        candidate_scores,
        job
    )

    print("\n" + "="*50)
    print("STEP 5: GENERATING FINAL ATS SCORE")
    print("="*50)
    print("\nATS SCORE RESULT:\n")

    print(
        json.dumps(
            ats_result,
            indent=2
        )
    )

    # 🔹 Step 6: Candidate Ranking

    candidates = [

        {
            "candidate_id": "C1",
            "final_score": 88
        },

        {
            "candidate_id": "C2",
            "final_score": 72
        },

        {
            "candidate_id": "C3",
            "final_score": 45
        },

        {
            "candidate_id": "C4",
            "final_score": 80
        }
    ]

    ranking_result = ranking_pipeline(
        candidates
    )

    print("\n" + "="*50)
    print("STEP 6: RANKING PIPELINE")
    print("="*50)
    print("\nRANKING RESULT:\n")

    print(
        json.dumps(
            ranking_result,
            indent=2
        )
    )

    # 🔹 Step 7: Resume Normalization

    normalized_text = normalize_resume_text(
        text
    )

    print("\nNORMALIZED RESUME:\n")

    print(normalized_text[:300])

    # 🔹 Step 8: Fairness Engine

    fair_candidates = [

        {
            "candidate_id": "C1",
            "final_score": 88,
            "skill_score": 85,
            "semantic_score": 82,
            "name": "John",
            "gender": "Male",
            "location": "NY"
        },

        {
            "candidate_id": "C2",
            "final_score": 72,
            "skill_score": 70,
            "semantic_score": 75,
            "name": "Alice",
            "gender": "Female",
            "location": "LA"
        }
    ]

    fair_candidates = normalize_scores(
        fair_candidates
    )

    for c in fair_candidates:

        mask_sensitive_data(c)

        generate_fair_score(c)

    print("\n" + "="*50)
    print("STEP 7: FAIRNESS & BIAS MITIGATION")
    print("="*50)
    print("\nFAIRNESS RESULT (PII MASKED):\n")

    print(
        json.dumps(
            fair_candidates,
            indent=2
        )
    )

    # 🔹 Step 9: Eligibility Decision Engine

    print("\n" + "="*50)
    print("STEP 8: ELIGIBILITY ENGINE DECISION")
    print("="*50)
    print("\nELIGIBILITY RESULT:\n")

    candidate_for_screening = {

        "candidate_id": "C123",

        "final_score": ats_result["final_score"],

        "skills": [
            "Python",
            "Django"
        ],

        "total_experience": 3,

        "location": "Bangalore",

        "available": True
    }

    rules = {

        "min_ats_score": 75,

        "mandatory_skills": [
            "Python"
        ],

        "min_experience": 2,

        "max_experience": 5,

        "allowed_locations": [
            "Bangalore"
        ],

        "availability_required": True
    }

    eligibility_result = evaluate_candidate(
        candidate_for_screening,
        rules
    )

    print(
        json.dumps(
            eligibility_result,
            indent=2
        )
    )

# -------------------------------
# RUN
# -------------------------------

if __name__ == "__main__":

    main()