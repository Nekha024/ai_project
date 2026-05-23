# Zecpath ATS AI – Technical Documentation

# 1. System Overview

The Zecpath ATS AI system automates candidate screening,
scoring, and ranking using AI + rule-based logic.

Core Objectives:
- Automate resume screening
- Improve hiring accuracy
- Reduce recruiter workload
- Ensure fairness and transparency

---

# 2. Core Modules

## Resume Parser

Purpose:
Extract text from PDF/DOCX resumes.

Files:
parsers/resume_reader.py

Features:
- PDF parsing
- DOCX support
- Text cleaning

---

## Section Segmentation

Purpose:
Identify sections:
- Skills
- Experience
- Education
- Projects
- Certifications

Files:
parsers/section_classifier.py

Approach:
- Rule-based detection
- NLP classification

---

## Skill Extraction Engine

Purpose:
Extract technical skills.

Files:
ats_engine/optimized_engine.py

Features:
- Fast keyword matching
- Cached processing
- Noise handling

---

## Semantic Matching Engine

Purpose:
Perform deep resume ↔ job matching using embeddings.

Files:
ats_engine/semantic_matcher.py

Uses:
- Sentence Transformers
- Cosine similarity

Measures:
- Skills similarity
- Experience similarity
- Project similarity

---

## ATS Scoring Engine

Purpose:
Generate explainable ATS score.

Files:
ats_engine/ats_scorer.py

Scoring Components:
- Skill score
- Experience score
- Education score
- Semantic score

---

## Ranking Engine

Purpose:
Rank and shortlist candidates.

Files:
ats_engine/ranking_engine.py

Outputs:
- Ranked list
- Top candidates
- Shortlisted candidates

---

## Fairness Engine

Purpose:
Reduce bias in hiring.

Files:
ats_engine/fairness_engine.py

Features:
- Score normalization
- Sensitive data masking
- Fair scoring

---

# 3. ATS Scoring Logic

Formula:

Final Score =
(Skill × Weight) +
(Experience × Weight) +
(Education × Weight) +
(Semantic × Weight)

Default Weights:
- Skills → 35%
- Experience → 25%
- Education → 15%
- Semantic → 25%

---

# 4. Shortlisting Rules

| Score | Status |
|---|---|
| ≥ 75 | Shortlisted |
| 50–74 | Review |
| <50 | Rejected |

---

# 5. System Advantages

- Modular architecture
- Explainable AI scoring
- Fast processing
- Semantic understanding
- Fairness support
- Recruiter-friendly outputs

---

# 6. Limitations

- Non-tech role understanding can improve
- Static weights in initial version
- Heavy NLP models require resources

---

# 7. Future Improvements

- Dynamic weight tuning
- Recruiter feedback loop
- Better soft-skill extraction
- Distributed processing
- GPU acceleration