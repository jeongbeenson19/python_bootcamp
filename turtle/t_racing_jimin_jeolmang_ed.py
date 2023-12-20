from turtle import Turtle, Screen
import random


def create_turtle(color, x, y):
    turtle = Turtle(shape='turtle')
    turtle.color(color)
    turtle.penup()
    turtle.setpos(x, y)
    return turtle


def jimin_picked_red():
    global jimin_is_red
    jimin_is_red = True
    return jimin_is_red


def jimin_picked_blue():
    global jimin_is_blue
    jimin_is_blue = True
    print("jimin is blue")
    return jimin_is_blue


def jimin_picked_yellow():
    global jimin_is_yellow
    jimin_is_yellow = True
    return jimin_is_yellow


def jimin_picked_green():
    global jimin_is_green
    jimin_is_green = True
    return jimin_is_green


jimin_is_red = False
jimin_is_green = False
jimin_is_yellow = False
jimin_is_blue = False

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

speed_list1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
               2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
               3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
               4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
               5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
               6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
               30
               ]
podium = []


def race():
    global race_end
    while not race_end:
        for color, char in racer_dict.items():
            if jimin_is_red:
                if color != 'red':
                    char.forward(1)
            if jimin_is_green:
                if color != 'green':
                    char.forward(1)
            if jimin_is_yellow:
                if color != 'yellow':
                    char.forward(1)
            if jimin_is_blue:
                if color != 'blue':
                    print("im not blue")
                    char.forward(1)
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
screen.listen()
screen.onkey(key='b', fun=jimin_picked_blue)
screen.onkey(key='y', fun=jimin_picked_yellow)
screen.onkey(key='r', fun=jimin_picked_red)
screen.onkey(key='g', fun=jimin_picked_green)
screen.onkey(key='space', fun=race)
screen.exitonclick()
