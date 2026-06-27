from flask import Flask, request, jsonify
from screening_ai.report_generators import generate_screening_report

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Screening AI API is running",
        "status": "success"
    })


@app.route("/screening/start", methods=["POST"])
def start_screening():
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "status": "error",
                "message": "No JSON data provided"
            }), 400

        candidate_id = data.get("candidate_id")
        job_id = data.get("job_id")

        if not candidate_id or not job_id:
            return jsonify({
                "status": "error",
                "message": "candidate_id and job_id are required"
            }), 400

        answers = data.get("answers", [])
        scores = data.get("scores", [])
        behavior_reports = data.get("behavior", [])

        report = generate_screening_report(
            candidate_id,
            job_id,
            answers,
            scores,
            behavior_reports
        )

        return jsonify({
            "status": "success",
            "report": report
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)