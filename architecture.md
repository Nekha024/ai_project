# ATS Architecture Diagram

## High-Level Architecture

```text
Frontend Dashboard
        ↓
Backend API Layer
        ↓
ATS AI Engine
 ├── Resume Parser
 ├── Section Segmenter
 ├── Semantic Matcher
 ├── ATS Scorer
 ├── Ranking Engine
 └── Fairness Engine
        ↓
Database / Storage
        ↓
Analytics & Reports
```

---

# Data Flow Diagram

```text
Resume Upload
      ↓
Text Extraction
      ↓
Section Segmentation
      ↓
Skill Extraction
      ↓
Semantic Matching
      ↓
ATS Scoring
      ↓
Ranking & Shortlisting
      ↓
Recruiter Dashboard
```

---

# API Interaction Flow

```text
Frontend → /resume/upload
Backend → /resume/parse
Backend → /ats/score
Backend → /ats/shortlist
Frontend ← Results
```