from screening_ai.stt_processor import (
    clean_transcript
)

def test_cleaning():

    text = "um i am a developer"

    result = clean_transcript(
        text
    )

    assert "um" not in result[
        "clean_text"
    ].lower()

    assert result[
        "clean_text"
    ].startswith("I")

    print(
        "STT cleaning test passed"
    )


if __name__ == "__main__":

    test_cleaning()