# Data Models

## Answer Object

```json
{
    "question_id":"Q1",
    "answer_text":"Worked on backend systems",
    "intent":"experience",
    "skills":["Python","Flask"],
    "communication_score":82,
    "confidence_score":78
}
```

---

## Report Object

```json
{
    "candidate_id":"C101",
    "scores":{
        "ats":80,
        "screening":76,
        "hr":84
    },
    "final_score":81,
    "decision":"Hire"
}
```