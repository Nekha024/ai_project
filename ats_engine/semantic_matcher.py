from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# -------------------------------
# Load Pretrained Embedding Model
# -------------------------------
model = SentenceTransformer('all-MiniLM-L6-v2')


# -------------------------------
# Generate Embeddings
# -------------------------------
def get_embedding(text):
    return model.encode(text, convert_to_numpy=True)


# -------------------------------
# Compute Similarity
# -------------------------------
def compute_similarity(text1, text2):

    emb1 = get_embedding(text1)
    emb2 = get_embedding(text2)

    similarity = cosine_similarity(
        [emb1],
        [emb2]
    )[0][0]

    return round(float(similarity), 4)


# -------------------------------
# Section-wise Matching
# -------------------------------
def match_resume_to_jd(resume, jd):

    results = {}

    # Skills Matching
    resume_skills = " ".join(
        resume.get("skills", [])
    )

    jd_skills = " ".join(
        jd.get("required_skills", [])
    )

    results["skills_similarity"] = compute_similarity(
        resume_skills,
        jd_skills
    )

    # Experience Matching
    resume_exp = " ".join([
        exp["role"]
        for exp in resume.get("experience", [])
    ])

    jd_role = jd.get("job_title", "")

    results["experience_similarity"] = compute_similarity(
        resume_exp,
        jd_role
    )

    # Project Matching
    resume_proj = " ".join([
        proj["description"]
        for proj in resume.get("projects", [])
    ])

    jd_desc = jd.get("job_description_text", "")

    results["project_similarity"] = compute_similarity(
        resume_proj,
        jd_desc
    )

    # Final Weighted Score
    final_score = (
        0.4 * results["skills_similarity"] +
        0.3 * results["experience_similarity"] +
        0.3 * results["project_similarity"]
    )

    results["final_similarity_score"] = round(
        final_score * 100,
        2
    )

    return results


# -------------------------------
# Threshold Classification
# -------------------------------
def classify_match(score):

    if score >= 85:
        return "Strong Match"

    elif score >= 65:
        return "Moderate Match"

    else:
        return "Weak Match"