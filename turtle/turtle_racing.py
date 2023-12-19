from turtle import Turtle, Screen
import random

red = Turtle(shape='turtle')
green = Turtle(shape='turtle')
blue = Turtle(shape='turtle')
yellow = Turtle(shape='turtle')

racer_list = [red, green, blue, yellow]
y = -100
red.color('red')
green.color('green')
blue.color('blue')
yellow.color('yellow')

for char in racer_list:
    char.penup()
    char.setpos(-250, y)
    y += 50

race_end = False
speed_list = [1, 1.5, 2, 3, 4, 5, 6, 7, 8, 9, 10]
podium = []

while not race_end:
    for char in racer_list:
        speed = random.choice(speed_list)
        char.forward(speed)
        status = char.pos()
        if status[0] >= 250:
            podium.append(char)
        if len(podium) == 3:
            race_end = True

print(podium)
screen = Screen()
screen.setup(width=500, height=400)
screen.exitonclick()
