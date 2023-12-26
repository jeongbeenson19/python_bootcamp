from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color('black')
        self.penup()
        self.lt(90)
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)
