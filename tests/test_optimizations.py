from ai_core.optimized_ai_engine import adjust_decision


def test_optimization():
    decision = adjust_decision(
        85,
        90,
        "High Risk"
    )

    assert decision == "Hold / Review"


if __name__ == "__main__":
    test_optimization()
    print("Optimization Test Passed ✅")