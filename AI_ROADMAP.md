# AI Project Roadmap: Future Phases

While the core ATS pipeline is functional and structurally sound, this roadmap outlines the strategic next steps required to take the Zecpath AI ATS from a functioning terminal script to a fully deployed SaaS product.

---

## Phase 1: API Integration & Persistence (Short-term)
The immediate next step is to connect the working logic in `main.py` to the FastAPI endpoints in `api/main.py`.

*   **Dynamic File Uploads**: Update the `/resume/upload` endpoint to accept actual PDF `UploadFile` objects, rather than returning mocked IDs.
*   **Database Integration**: Implement a lightweight database (e.g., SQLite using SQLAlchemy) to persist uploaded resumes, job descriptions, and calculated ATS scores.
*   **Remove Mocked Data**: Replace the hardcoded JSON responses in the API with real-time calls to the `ats_engine` and `screening_ai` modules.

## Phase 2: AI Interviewer Expansion (Mid-term)
The original project scope included ambitious plans for an automated AI Interview system (found in the deprecated `interview_ai` modules). This should be revived as a Phase 2 feature.

*   **Question Generation**: Use Large Language Models (LLMs) to dynamically generate technical and behavioral interview questions based on the candidate's specific resume and ATS score.
*   **Speech-to-Text (STT)**: Integrate models like OpenAI Whisper to transcribe spoken candidate answers during a live automated interview.
*   **Answer Evaluation**: Build an engine to semantically evaluate the candidate's spoken answers against a rubric of expected technical concepts.

## Phase 3: Frontend Web Dashboard (Long-term)
To make the system usable by HR professionals, a graphical user interface is required.

*   **Recruiter Dashboard**: Build a React or Next.js web application that consumes the FastAPI endpoints.
*   **Visualizations**: Create charts showing the breakdown of a candidate's ATS score (Skill vs. Experience vs. Semantic Match).
*   **Pipeline Management**: Allow recruiters to drag-and-drop candidates between columns (Applied → Shortlisted → Interviewing → Offered).

## Phase 4: Cloud Deployment & Scaling (Future)
*   **Containerization**: Wrap the FastAPI backend and HuggingFace models in Docker containers.
*   **Cloud Hosting**: Deploy the API to AWS (EC2/Lambda) or Google Cloud Run, utilizing GPU instances for faster NLP inference if necessary.
