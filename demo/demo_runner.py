from interview_ai.final_hr_module import run_hr_interview

answers = [

    {
        "question_id": "Q1",
        "relevance_score": 0.90,
        "communication_score": 82,
        "confidence_score": 78,
        "contradiction": False,
        "is_vague": False
    },

    {
        "question_id": "Q2",
        "relevance_score": 0.85,
        "communication_score": 80,
        "confidence_score": 75,
        "contradiction": False,
        "is_vague": False
    }

]

communication = {
    "communication_score": 82
}

behavior = {

    "confidence": {
        "confidence_score": 78
    },

    "behavioral_score": 80,

    "contradiction": False

}

result = run_hr_interview(

    "C1001",

    answers,

    communication,

    behavior

)

print(result)