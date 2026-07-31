"""
Data Retention Policy
"""

from datetime import datetime, timedelta


RETENTION_DAYS = 90


def retention_details():

    today = datetime.today()

    delete_date = today + timedelta(
        days=RETENTION_DAYS
    )

    return {

        "retention_period_days": RETENTION_DAYS,

        "created_on": today.strftime("%Y-%m-%d"),

        "delete_after": delete_date.strftime("%Y-%m-%d"),

        "policy":
            "Delete or anonymize after 90 days."
    }