ROLE_SKILLS = {

    "mern_developer": [

        "JavaScript",

        "React",

        "Node.js",

        "MongoDB"

    ],

    "python_developer": [

        "Python",

        "Flask",

        "Django",

        "REST API"

    ],

    "java_developer": [

        "Java",

        "Spring Boot",

        "Microservices"

    ],

    "devops_engineer": [

        "Docker",

        "Kubernetes",

        "AWS"

    ]

}


def get_skills(role):

    return ROLE_SKILLS.get(role, [])