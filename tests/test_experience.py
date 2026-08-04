from technical_ai.experience_logic import get_experience_level


def test_experience():

    assert get_experience_level(1) == "0-2"

    assert get_experience_level(3) == "3-5"

    assert get_experience_level(7) == "5+"