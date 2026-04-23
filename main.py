import json
from scoring.score import calculate_final_score


def load_json(path):
    with open(path, "r") as f:
        return json.load(f)


def main():
    candidate = load_json("data/resume.json")
    job = load_json("data/job.json")

    score = calculate_final_score(candidate, job)

    print(f"Final Candidate Score: {score}%")


if __name__ == "__main__":
    main()