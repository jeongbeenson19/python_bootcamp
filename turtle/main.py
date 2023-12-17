from turtle import Turtle, Screen
from action import Action

timmy_the_turtle = Action()
# timmy_the_turtle.square(100, "right")
# timmy_the_turtle.dashed_line(15)
timmy_the_turtle.regular_polygon(10, 100)


screen = Screen()
screen.exitonclick()
