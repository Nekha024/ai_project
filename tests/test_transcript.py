from screening_ai.transcript_normalizer import (
    normalize_transcript
)

text = "Um I have 3 years experience"

result = normalize_transcript(text)

print(result)

assert "um" not in result