from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "Zecpath ATS API Running"
    }


# -------------------------------
# Resume Upload API
# -------------------------------

@app.post("/resume/upload")
def upload_resume():

    return {

        "status": "success",

        "message":
        "Resume uploaded successfully",

        "resume_id": "R456"
    }


# -------------------------------
# Resume Parsing API
# -------------------------------

@app.post("/resume/parse")
def parse_resume():

    return {

        "candidate_id": "C123",

        "parsed_profile": {

            "skills": [
                "Python",
                "Django"
            ],

            "education": [],

            "experience": []
        },

        "status": "completed"
    }


# -------------------------------
# ATS Scoring API
# -------------------------------

@app.post("/ats/score")
def ats_score():

    return {

        "candidate_id": "C123",

        "final_score": 86.5,

        "breakdown": {

            "skills": 90,

            "experience": 85,

            "education": 80,

            "semantic": 88
        }
    }


# -------------------------------
# Shortlisting API
# -------------------------------

@app.post("/ats/shortlist")
def shortlist():

    return {

        "job_id": "J123",

        "total_candidates": 50,

        "shortlisted": 20,

        "candidates": [

            {

                "candidate_id": "C123",

                "score": 88,

                "status": "Shortlisted"
            }
        ]
    }


# uvicorn api.main:app --reload