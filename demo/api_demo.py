import requests

BASE = "http://127.0.0.1:5000/api/hr"


response = requests.post(

    BASE + "/start",

    json={

        "candidate_id": "C101",

        "job_id": "J501",

        "role_type": "technical",

        "experience_level": "fresher"

    }

)

print(response.json())