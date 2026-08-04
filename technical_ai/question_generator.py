import random


QUESTION_BANK = {

    "Python": {

        "basic": [

            "What is Python?",

            "Explain List and Tuple."

        ],

        "intermediate": [

            "Explain decorators.",

            "What is GIL?"

        ],

        "advanced": [

            "Design a scalable REST API.",

            "Explain multiprocessing architecture."

        ]

    },

    "JavaScript": {

        "basic": [

            "Difference between let and var.",

            "What is Hoisting?"

        ],

        "intermediate": [

            "Explain Closures.",

            "Explain Event Loop."

        ],

        "advanced": [

            "Design scalable frontend architecture."

        ]

    }

}


def generate_question(

        skill,

        difficulty

):

    questions = QUESTION_BANK.get(

        skill,

        {}

    ).get(

        difficulty,

        ["Question unavailable"]

    )

    return random.choice(questions)