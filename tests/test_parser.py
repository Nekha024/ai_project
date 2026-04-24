from parsers.resume_reader import extract_resume_text

def test_parser():
    text = extract_resume_text("data/sample_resume.pdf")
    assert len(text) > 0