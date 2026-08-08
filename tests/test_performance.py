def test_performance():
    from ai_core.performance_optimized import fast_decision

    result = fast_decision(80)

    assert result == "Selected"