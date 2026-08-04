"""
Technical Evaluation Report Generator
"""


def generate_technical_report(candidate_id,
                              technical_result):

    score = technical_result["final_score"]

    if score >= 80:
        decision = "Strong Technical Fit"

    elif score >= 60:
        decision = "Consider"

    else:
        decision = "Weak Technical Fit"

    strengths = []

    weaknesses = []

    breakdown = technical_result["details"]["breakdown"]

    if breakdown["accuracy"] >= 0.8:
        strengths.append("Correct technical understanding")

    else:
        weaknesses.append("Incorrect concepts")

    if breakdown["depth"] >= 0.8:
        strengths.append("Deep explanation")

    else:
        weaknesses.append("Needs deeper explanation")

    if breakdown["logic"] >= 0.8:
        strengths.append("Good logical reasoning")

    if breakdown["real_world"] >= 0.8:
        strengths.append("Good production knowledge")

    return {

        "candidate_id":candidate_id,

        "technical_score":score,

        "decision":decision,

        "strengths":strengths,

        "weaknesses":weaknesses,

        "breakdown":breakdown

    }