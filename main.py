import json
from scoring.score import calculate_final_score
from parsers.resume_reader import extract_resume_text



def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

def save_text(text):
    with open("data/cleaned_resume.txt", "w") as f:
        f.write(text)

def main():
    # 🔹 Step 1: Extract text from resume
    file_path = "data/sample_resume.pdf"  # or .docx
    text = extract_resume_text(file_path)

    print("Extracted Text Preview:\n")
    print(text[:300])

    save_text(text)

    # 🔹 Step 2: Load structured data
    candidate = load_json("data/resume.json")
    job = load_json("data/job.json")

    # 🔹 Step 3: Calculate score
    score = calculate_final_score(candidate, job)

    print(f"\nFinal Candidate Score: {score}%")



if __name__ == "__main__":
    main()