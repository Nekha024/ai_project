from flask import jsonify


def error_response(message, status=400):

    return jsonify(
        {
            "status": "error",
            "error_code": "INVALID_INPUT",
            "message": message
        }
    ), status