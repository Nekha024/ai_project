# Final Internship Portfolio Report
**Project Name:** Zecpath AI Applicant Tracking System
**Author:** Nekha A
**Role:** AI Intern

---

## 1. Executive Summary
During the course of this internship, I architected and developed an **AI-powered Applicant Tracking System (ATS)**. The primary objective of this project was to solve the inefficiencies of traditional recruitment by automating the resume screening process using advanced Natural Language Processing (NLP) and machine learning.

The final deliverable is a robust, modular Python pipeline that ingests candidate resumes, extracts semantic meaning, scores them against job descriptions, and applies fairness filters to ensure unbiased hiring.

## 2. System Architecture
The system was designed with a highly modular architecture, separating data extraction from AI processing and final decision logic. 

The pipeline flows through the following stages:
1. **Parser Engine (`parsers/`)**: Ingests PDF documents and extracts raw text. A section classifier then segments the text into structured blocks (Skills, Experience, Education) using regex and NLP markers.
2. **ATS Engine (`ats_engine/`)**: The core brain of the system. 
   - Uses **HuggingFace Transformers** to generate semantic embeddings of the candidate's skills and the job requirements.
   - Calculates a `semantic_similarity_score` using cosine similarity.
   - Blends this with traditional keyword matching to generate a weighted final ATS score.
3. **Screening AI (`screening_ai/`)**:
   - **Fairness Engine**: Masks personally identifiable information (PII) such as names and genders to ensure the final ranking is purely merit-based.
   - **Eligibility Engine**: Evaluates the candidate against strict business rules (e.g., minimum years of experience, remote availability) to output a definitive status (`Shortlisted`, `Review`, `Rejected`).

## 3. Key Achievements & Deliverables
- **End-to-End Pipeline**: Successfully built and demonstrated a functioning terminal pipeline (`main.py`) that processes a candidate from raw PDF to final ranked decision.
- **Semantic Understanding**: Moved beyond basic keyword matching by integrating transformer-based semantic analysis, allowing the system to recognize that "Frontend Developer" and "React Engineer" are related concepts.
- **Codebase Optimization**: Conducted a massive codebase refactor in the final weeks, purging over 100 iterative draft files and organizing the repository into a clean, production-ready structure.
- **API Foundation**: Laid the groundwork for a web-facing product by building a FastAPI skeleton (`api/main.py`) that outlines the REST endpoints needed for frontend integration.

## 4. Skills Acquired
- **Python Development**: Advanced structuring, modularity, and dependency management.
- **AI & NLP Integration**: Utilizing HuggingFace models for semantic text analysis.
- **Software Architecture**: Designing stateless pipelines and structuring large codebases.
- **API Design**: Building RESTful interfaces using FastAPI.

## 5. Conclusion
This internship provided hands-on experience in solving real-world business problems using Artificial Intelligence. The Zecpath AI ATS is not just a proof-of-concept; its modular design ensures that it can be directly wired into a web frontend and scaled into a production recruitment tool.
