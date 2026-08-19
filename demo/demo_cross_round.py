from ai_core.aggregation_pipeline import aggregation_pipeline

scores = {

    "ats": 75,

    "screening": 70,

    "hr": 80,

    "technical": 85,

    "machine_test": 78

}

result = aggregation_pipeline(

    candidate_id="C9001",

    scores=scores,

    role_type="technical"

)

print(result)