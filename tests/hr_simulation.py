import random


CANDIDATE_RANGES = {

    "Confident": (80, 95),

    "Hesitant": (55, 70),

    "Inexperienced": (50, 65),

    "Overqualified": (75, 90)

}


def simulate_candidate(candidate_type):

    low, high = CANDIDATE_RANGES[candidate_type]

    ai_score = random.randint(low, high)

    human_score = ai_score + random.randint(-5, 5)

    if ai_score >= 75:

        ai_decision = "Strong Hire"

    elif ai_score >= 55:

        ai_decision = "Consider"

    else:

        ai_decision = "Reject"

    if human_score >= 75:

        human_decision = "Strong Hire"

    elif human_score >= 55:

        human_decision = "Consider"

    else:

        human_decision = "Reject"

    return {

        "candidate_type": candidate_type,

        "ai_score": ai_score,

        "human_score": human_score,

        "decision_ai": ai_decision,

        "decision_human": human_decision

    }


def run_simulation():

    types = [

        "Confident",

        "Hesitant",

        "Inexperienced",

        "Overqualified"

    ]

    results = []

    for _ in range(40):

        candidate = random.choice(types)

        results.append(

            simulate_candidate(candidate)

        )

    return results