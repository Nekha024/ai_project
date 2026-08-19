# Zecpath AI Applicant Tracking System (ATS)

An advanced, AI-powered Applicant Tracking System that automates the recruitment pipeline by analyzing candidate resumes, understanding semantic meaning via NLP, and matching them against Job Descriptions.

Developed by **Nekha A** during the AI Internship program.

---

## 🚀 Features

- **Automated Resume Parsing**: Extracts raw text and intelligently segments it into Experience, Skills, and Profile blocks.
- **Semantic Matching**: Utilizes HuggingFace Transformer models to understand the *meaning* and context of a candidate's experience, going far beyond traditional keyword matching.
- **Dynamic ATS Scoring**: Calculates a weighted final score blending traditional keyword hits with deep semantic understanding.
- **Fairness & Bias Engine**: Automatically masks personally identifiable information (PII) such as Name, Gender, and Location before generating a fair candidate score.
- **Eligibility Engine**: Enforces hard constraints (e.g., minimum experience years, location availability) to instantly categorize candidates as `Shortlisted`, `Review`, or `Rejected`.

---

## 📁 Project Structure

```
project_root/
│
├── ai_core/             # Core AI configuration and aggregation logic
├── api/                 # FastAPI backend for web integration (Future)
├── ats_engine/          # Core scoring, semantic matching, and ranking algorithms
├── data/                # Sample resumes, JDs, and output JSON files
├── parsers/             # Text extraction and document segmentation
├── screening_ai/        # Fairness masking, eligibility rules, and report generation
├── main.py              # 🚀 Main entry point for the ATS Pipeline Demo
├── requirements.txt     # Project dependencies
├── FINAL_REPORT.md      # Detailed internship architecture and delivery report
└── AI_ROADMAP.md        # Future implementation phases
```

---

## ⚙️ Setup Instructions

This project requires **Python 3.9+**. 

### 1. Create a Virtual Environment
It is highly recommended to run this project inside a virtual environment to manage dependencies securely.
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

### 2. Install Dependencies
Install all required machine learning models, FastAPI, and parsing libraries.
```powershell
pip install -r requirements.txt
```

---

## 💻 Running the Application

### The Core AI Pipeline Demo
To run the end-to-end AI pipeline (Parsing → Matching → Scoring → Fairness → Eligibility) on the sample candidate data, execute the main script:

```powershell
python main.py
```
*Note: The first time you run this, it may take a moment to download the HuggingFace semantic models.*

### The API Server (Mocked Preview)
A FastAPI backend skeleton is included in `api/main.py` for future web integration. You can start the server to view the interactive API docs:
```powershell
uvicorn api.main:app --reload
```
Then visit `http://127.0.0.1:8000/docs` in your browser.

---

## 📝 License & Authorship

Developed entirely by **Nekha A**.
Submitted as the final deliverable for the AI Internship Program.
