from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.write(f"score: {self.score}")

    def get_score(self):
        self.score += 1
