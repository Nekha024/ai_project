LEVELS = [

    "basic",

    "intermediate",

    "advanced"

]


def adjust_difficulty(

        current_level,

        answer_quality

):

    index = LEVELS.index(current_level)

    if answer_quality == "good" and index < 2:

        return LEVELS[index + 1]

    if answer_quality == "poor" and index > 0:

        return LEVELS[index - 1]

    return current_level