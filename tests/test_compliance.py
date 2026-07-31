from ethics.consent_manager import (
    collect_consent,
    has_valid_consent
)

from ethics.fairness_checker import (
    remove_demographic_fields
)

from ethics.compliance import compliance_report


def test_consent():

    consent = collect_consent("C1")

    assert has_valid_consent(consent)


def test_demographic_removal():

    data = {

        "gender": "Male",

        "skills": ["Python"]

    }

    cleaned = remove_demographic_fields(data)

    assert "gender" not in cleaned


def test_compliance():

    report = compliance_report()

    assert report["secure_storage"] is True