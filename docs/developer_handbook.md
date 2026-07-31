# Developer Integration Guide

## Integration Steps

1. Call POST /start

2. Receive interview questions

3. Ask questions

4. Send answers using POST /answer

5. Continue interview

6. Call GET /report

7. Display recruiter report

---

## Technology Stack

Backend
- Python

Framework
- Flask

Database
- PostgreSQL

AI
- NLP
- Rule Based
- ML Models

---

## Folder Overview

api/
interview_ai/
screening_ai/
ai_core/
tests/
docs/

---

## Best Practices

Validate all requests

Use HTTPS

Log API errors

Cache repeated requests

Enable authentication