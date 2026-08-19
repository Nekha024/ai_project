from ai_core.recommendation_pipeline import recommendation_pipeline

scores = {

    "final_score": 82,

    "technical": 88,

    "communication": 80,

    "behavior": 75,

    "integrity": 85

}

result = recommendation_pipeline(

    candidate_id="C10001",

    scores=scores,

    behavior_risk="Low Risk",

    integrity_risk="Moderate Risk"

)

print(result)