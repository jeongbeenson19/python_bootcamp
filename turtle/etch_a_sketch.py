from turtle import Turtle, Screen

tim = Turtle()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_left():
    tim.lt(5)


def turn_right():
    tim.rt(5)


def clear():
    tim.clear()
    tim.penup()
    tim.setpos(0, 0)
    tim.setheading(0)
    tim.pendown()


screen = Screen()
screen.listen()
screen.onkey(fun=move_forward, key='w')
screen.onkey(fun=move_backward, key='s')
screen.onkey(fun=turn_left, key='a')
screen.onkey(fun=turn_right, key='d')
screen.onkey(fun=clear, key='c')
screen.exitonclick()