from ai_core.report_pipeline import hiring_report_pipeline
from ai_core.report_export import export_json

candidate = {

    "candidate_id": "C12001",

    "ats": 78,

    "screening": 72,

    "hr": 80,

    "technical": 85,

    "machine_test": 76,

    "behavior": {

        "confidence": 82,

        "risk_level": "Low Risk",

        "integrity": "Moderate Risk"

    },

    "decision": "Selected"

}

report = hiring_report_pipeline(candidate)

print(report)

export_json(report)