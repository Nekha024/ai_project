class InterviewState:

    def __init__(

            self,

            candidate_id,

            role,

            experience

    ):

        self.candidate_id = candidate_id

        self.role = role

        self.experience = experience

        self.current_difficulty = "basic"

        self.questions = []

        self.scores = []

        self.status = "started"

    def add_question(

            self,

            question

    ):

        self.questions.append(question)

    def add_score(

            self,

            score

    ):

        self.scores.append(score)

    def finish(self):

        self.status = "completed"