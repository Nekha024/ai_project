# ATS Developer Guide

# 1. Project Setup

Clone Project:

```bash
git clone repo
cd ats-system
```

Install Requirements:

```bash
pip install -r requirements.txt
```

---

# 2. Run System

```bash
python main.py
```

---

# 3. Project Structure

```text
project/
│
├── ats_engine/
├── parsers/
├── scoring/
├── tests/
├── docs/
├── data/
└── main.py
```

---

# 4. Important Modules

| Module | Purpose |
|---|---|
| resume_reader.py | Extract resume text |
| section_classifier.py | Resume segmentation |
| semantic_matcher.py | Semantic similarity |
| ats_scorer.py | ATS score generation |
| ranking_engine.py | Ranking & shortlisting |
| fairness_engine.py | Bias reduction |
| optimized_engine.py | Performance tuning |

---

# 5. Run Tests

```bash
pytest tests/
```

OR

```bash
python -m tests.test_ats_scorer
```

---

# 6. Add New Skills

Example:

```python
SKILLS.append("kubernetes")
```

---

# 7. Add New Role Weights

Example:

```python
ROLE_WEIGHTS["devops engineer"] = {
    "skills": 0.4,
    "experience": 0.3,
    "education": 0.1,
    "semantic": 0.2
}
```

---

# 8. Logging

Supported Levels:
- INFO
- WARNING
- ERROR
- DEBUG

---

# 9. Best Practices

- Keep modules independent
- Validate all JSON inputs
- Use caching for performance
- Test every new module

---

# 10. Future Improvements

- FastAPI integration
- Recruiter dashboard
- Distributed processing
- Cloud deployment