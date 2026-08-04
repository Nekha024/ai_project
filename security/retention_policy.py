RETENTION_POLICY = {
    "resume": 90,
    "transcript": 60,
    "report": 120,
    "audit_log": 180
}


def get_retention_days(data_type):
    return RETENTION_POLICY.get(data_type)


if __name__ == "__main__":

    print(get_retention_days("resume"))