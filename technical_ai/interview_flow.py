from technical_ai.role_mapper import get_skills

from technical_ai.question_generator import generate_question

from technical_ai.experience_logic import get_experience_level


def technical_interview(

        role,

        experience_years

):

    level = get_experience_level(

        experience_years

    )

    skills = get_skills(role)

    difficulty = {

        "0-2": "basic",

        "3-5": "intermediate",

        "5+": "advanced"

    }[level]

    questions = []

    for skill in skills:

        questions.append(

            generate_question(

                skill,

                difficulty

            )

        )

    return {

        "experience_level": level,

        "difficulty": difficulty,

        "questions": questions

    }