# AI Recruitment System

## Overview

This project is a basic AI-powered recruitment system that analyzes candidate resumes and matches them with job descriptions using structured data and scoring logic.

---

## Features

* Resume data converted into structured JSON format
* Job description structured into JSON
* Skill-based matching
* Experience-based matching
* Final candidate scoring system

---

## Project Structure

```
project_root/
│
├── data/                # Sample resume and job data
├── parsers/             # Resume parsing (future work)
├── ats_engine/          # Main pipeline (future expansion)
├── screening_ai/        # AI filtering logic
├── interview_ai/        # Interview logic (future)
├── scoring/             # Scoring system
├── utils/               # Helper functions (logger etc.)
├── tests/               # Test cases
│
├── main.py              # Entry point
├── README.md
├── DATA_MODEL.md        # Data structure documentation
├── requirements.txt
```

---

## Setup

1. Create virtual environment:

```
python -m venv venv
venv\Scripts\Activate.ps1
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the project:

```
python main.py
```

---

## Data Design

This project uses structured JSON formats:

### Resume Schema

Contains candidate information such as:

* name
* skills
* experience

### Job Schema

Defines job requirements such as:

* required skills
* experience required

### Matching Logic

The system calculates score based on:

* Skill match
* Experience match

---

## Example Output

```
Final Candidate Score: 65.0%
```

---

## Author

Nekha A
