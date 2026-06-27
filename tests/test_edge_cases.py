from screening_ai.robust_flow import (
    detect_edge_case
)


def test_missing():

    result = detect_edge_case(
        "",
        1.0
    )

    assert result == "missing"


def test_poor_audio():

    result = detect_edge_case(
        "hello",
        0.4
    )

    assert result == "poor_audio"


def test_language_mix():

    result = detect_edge_case(
        "hai chetta",
        1.0
    )

    assert result == "language_mix"


def test_valid():

    result = detect_edge_case(
        "I have three years experience",
        1.0
    )

    assert result == "valid"