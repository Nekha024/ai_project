import json


def export_json(report, filename="candidate_report.json"):

    with open(filename, "w") as file:

        json.dump(report, file, indent=4)

    print("Report exported successfully.")