#Education Relevance Logic

def compute_education_relevance(education_list, job_description):
    score = 0

    job_desc = job_description.lower()

    for edu in education_list:
        field = edu["field"]

        if field in job_desc:
            score += 1

        if edu["degree"] == "master":
            score += 0.5

        if edu["degree"] == "phd":
            score += 1

    return round(score, 2)