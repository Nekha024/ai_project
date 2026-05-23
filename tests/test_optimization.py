from ats_engine.optimized_engine import (
    fast_skill_extract
)


def test_fast_skill():

    text = "Python React Developer"

    result = fast_skill_extract(text)

    assert "python" in result
    assert "react" in result

    print("Optimization test passed!")


test_fast_skill()