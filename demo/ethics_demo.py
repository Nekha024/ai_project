from ethics.consent_manager import collect_consent
from ethics.fairness_checker import (
    remove_demographic_fields,
    fairness_review
)
from ethics.explainability import generate_explanation
from ethics.compliance import compliance_report
from ethics.retention_policy import retention_details


def run_demo():

    candidate = {

        "name": "John",

        "gender": "Male",

        "age": 25,

        "skills": [
            "Python",
            "Flask"
        ]
    }

    print("\n===== Consent =====")

    consent = collect_consent(
        "C1001"
    )

    print(consent)

    print("\n===== Fairness =====")

    print(remove_demographic_fields(candidate))

    print(fairness_review())

    print("\n===== Explainability =====")

    print(

        generate_explanation(

            ats_score=82,

            screening_score=75,

            hr_score=85

        )

    )

    print("\n===== Compliance =====")

    print(compliance_report())

    print("\n===== Retention =====")

    print(retention_details())


if __name__ == "__main__":
    run_demo()