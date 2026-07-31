# HR Interview API Specification

## Base URL

```
http://localhost:5000/api/hr
```

---

## Start Interview

POST /start

### Request

```json
{
  "candidate_id":"C101",
  "job_id":"J501",
  "role_type":"technical",
  "experience_level":"fresher"
}
```

### Response

```json
{
  "session_id":"S101",
  "questions":[
      "Tell me about yourself",
      "What are your strengths?"
  ]
}
```

---

## Submit Answer

POST /answer

### Request

```json
{
  "session_id":"S101",
  "question_id":"Q1",
  "answer":"I have worked on Python projects.",
  "duration":6
}
```

### Response

```json
{
    "follow_up":"Can you explain more?",
    "next_question":"Describe teamwork experience."
}
```

---

## Get Report

GET /report/<session_id>

### Response

```json
{
    "candidate_id":"C101",
    "final_score":82,
    "decision":"Strong Hire"
}
```