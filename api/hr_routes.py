from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/api/hr/start", methods=["POST"])
def start():

    return jsonify({

        "session_id": "S101",

        "questions": [

            "Tell me about yourself",

            "What are your strengths?"

        ]

    })


@app.route("/api/hr/answer", methods=["POST"])
def answer():

    return jsonify({

        "follow_up":
        "Can you explain more?",

        "next_question":
        "Describe teamwork experience."

    })


@app.route("/api/hr/report/<session_id>")
def report(session_id):

    return jsonify({

        "candidate_id": "C101",

        "final_score": 82,

        "decision": "Strong Hire"

    })


if __name__ == "__main__":

    app.run(debug=True)