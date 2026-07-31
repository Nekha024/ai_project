# Zecpath HR Interview AI – System Architecture

## High-Level Architecture

```
Frontend (Web / Mobile)
        │
        ▼
Backend API Layer
        │
        ▼
---------------------------------------
HR Interview AI Engine
---------------------------------------
1. Question Generator
2. Conversation Engine
3. Follow-Up Engine
4. Answer Understanding Engine
5. Communication Analyzer
6. Confidence & Behavior Analyzer
7. HR Scoring Engine
8. Aptitude Engine
9. Summary Generator
---------------------------------------
        │
        ▼
Database / Storage
```

## Data Flow

```
Candidate Voice/Text
        │
        ▼
Speech-To-Text
        │
        ▼
Answer Processing
        │
        ▼
AI Analysis
        │
        ▼
Score Generation
        │
        ▼
Recruiter Report
```

## Core Modules

| Module | Responsibility |
|---------|---------------|
| Question Generator | Generate HR Questions |
| Conversation Engine | Manage Interview Flow |
| NLP Engine | Understand Responses |
| Communication Engine | Analyze Fluency & Grammar |
| Confidence Analyzer | Detect Confidence |
| HR Scoring | Generate HR Score |
| Aptitude Engine | Logical Reasoning |
| Summary Generator | Recruiter Report |