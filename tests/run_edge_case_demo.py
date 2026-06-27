from screening_ai.robust_flow import (
    detect_edge_case,
    handle_edge_case
)

from screening_ai.error_framework import (
    get_error_response
)

samples = [

    ("", 1.0),

    ("hello", 0.4),

    ("um", 1.0),

    ("hai chetta", 1.0),

    ("python", 1.0),

    ("I have 3 years experience", 1.0)
]

for answer, confidence in samples:

    issue = detect_edge_case(
        answer,
        confidence
    )

    action = handle_edge_case(
        None,
        answer,
        confidence,
        0
    )

    print("\nAnswer:", answer)
    print("Issue:", issue)
    print("Action:", action)
    print(
        "Message:",
        get_error_response(issue)
    )