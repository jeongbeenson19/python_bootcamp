from turtle import Turtle, Screen
import random


def create_turtle(color, x, y):
    turtle = Turtle(shape='turtle')
    turtle.color(color)
    turtle.penup()
    turtle.setpos(x, y)
    return turtle


red = create_turtle('red', -500, -100)
green = create_turtle('green', -500, -50)
blue = create_turtle('blue', -500, 0)
yellow = create_turtle('yellow', -500, 50)

racer_dict = {'red': red, 'green': green, 'blue': blue, 'yellow': yellow}

race_end = False
speed_list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
              2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
              3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
              4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
              5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
              6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
              30
              ]
podium = []

while not race_end:
    for color, char in racer_dict.items():
        speed = random.choice(speed_list)
        char.forward(speed)
        status = char.pos()
        if status[0] > 500:
            if color not in podium:
                podium.append(color)
        if len(podium) == 3:
            race_end = True

print("Podium:", podium)

screen = Screen()
screen.setup(width=500, height=400)
screen.exitonclick()
