from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.goto(-240, 260)
        self.hideturtle()
        self.level = 1

    def score(self):
        self.clear()
        self.write(f"level: {self.level}", font=FONT, align='center')

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", font= FONT, align="center")
