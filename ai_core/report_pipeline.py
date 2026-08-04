from ai_core.hiring_report_generator import generate_hiring_report


def hiring_report_pipeline(data):

    report = generate_hiring_report(

        candidate_id=data["candidate_id"],

        ats=data["ats"],

        screening=data["screening"],

        hr=data["hr"],

        technical=data["technical"],

        machine_test=data["machine_test"],

        behavior=data["behavior"],

        decision=data["decision"]

    )

    return report