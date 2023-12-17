class QuizBrain:
    def __init__(self, q_bank):
        self.question_number = 0
        self.question_list = q_bank
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)-1

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number + 1}: {current_question.text}. (True/False)?: ").lower()
        self.question_number += 1
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, users_answer, answer):
        if users_answer.capitalize() == answer:
            self.score += 1
            print("you're right")
            print(f"you're current score is {self.score}/{self.question_number} ")
        else:
            print("you're wrong")
            print(f"correct answer is {answer}")
            print(f"you're current score is {self.score}/{self.question_number} ")
