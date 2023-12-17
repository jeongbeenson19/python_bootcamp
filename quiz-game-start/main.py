from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
q_data = question_data


def make_question(data):
    q_list = []
    for question in data:
        q = Question(question["text"], question["answer"])
        q_list.append(q)
    return q_list


question_bank = make_question(q_data)
quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print(f"you're final score is {quiz.score}")
