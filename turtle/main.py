from turtle import Turtle, Screen
from action import Action

timmy_the_turtle = Action()
# timmy_the_turtle.square(100, "right")
# timmy_the_turtle.dashed_line(15)
# timmy_the_turtle.regular_polygon(10, 100)
# timmy_the_turtle.random_walk(2500)
# timmy_the_turtle.spirograph(100, 150)

timmy_the_turtle.hirst_painting(3)

screen = Screen()
screen.colormode(255)
screen.exitonclick()
