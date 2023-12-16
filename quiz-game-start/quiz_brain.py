class QuizBrain:
    def __init__(self, q_bank):
        self.question_number = 0
        self.question_list = q_bank

    def still_has_question(self):
        return self.question_number < len(self.question_list - 1)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        input(f"Q.{self.question_number + 1}: {current_question.text}. (True/False)?: ")
        self.question_number += 1
        return self.question_number


