from turtle import Turtle, Screen


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.computer_score = 0
        self.user_score = 0
        self.color('grey')
        self.hideturtle()
        self.penup()
        self.screen = Screen()
        self.font_setup = ('Arial', 150, 'normal')
        self.goto(0, -75)
        self.write(":", font=self.font_setup, align='center')
        self.update_score()

    def update_score(self):
        self.goto(-175, -75)
        self.write(self.user_score, font=self.font_setup, align='center')
        self.goto(175, -75)
        self.write(self.computer_score, font=self.font_setup, align='center')

    def user_get_score(self):
        self.user_score += 1
        self.clear()
        self.update_score()

    def computer_get_score(self):
        self.computer_score += 1
        self.clear()
        self.update_score()
