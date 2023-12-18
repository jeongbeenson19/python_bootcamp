from turtle import Turtle
import random
from color import ColorGram


class Action:
    def __init__(self):
        self.timmy_the_turtle = Turtle()
        self.colors = ColorGram()

    def random_color(self):
        r = random.random()  # 빨강 채널
        g = random.random()  # 초록 채널
        b = random.random()  # 파랑 채널
        self.timmy_the_turtle.pencolor(r, g, b)

    def random_color_dot(self, size):
        r = random.random()  # 빨강 채널
        g = random.random()  # 초록 채널
        b = random.random()  # 파랑 채널
        new_color = (r, g, b)
        self.timmy_the_turtle.dot(size, new_color)

    def square(self, distance_of_each_line, direction):
        for n in range(0, 4):
            self.timmy_the_turtle.forward(distance_of_each_line)
            if direction == "right":
                self.timmy_the_turtle.rt(90)
            else:
                self.timmy_the_turtle.lt(90)

    def dashed_line(self, repetitions):
        for n in range(repetitions):
            self.timmy_the_turtle.forward(10)
            self.timmy_the_turtle.penup()
            self.timmy_the_turtle.forward(10)
            self.timmy_the_turtle.pendown()

    def regular_polygon(self, number_of_angle, length_of_each_line):
        for n in range(3, number_of_angle + 1):
            self.random_color()
            for m in range(n):
                degrees = 360 / n
                self.timmy_the_turtle.rt(degrees)
                self.timmy_the_turtle.forward(length_of_each_line)

    def random_walk(self, repetitions):
        direction = [0, 90, 180, 270]
        output = [0, 0, 0, 0]
        self.timmy_the_turtle.pensize(5)
        self.timmy_the_turtle.speed(20)
        for n in range(repetitions):
            random_input = random.randint(0, 3)
            self.random_color()
            output[random_input] += 1
            self.timmy_the_turtle.rt(direction[random_input])
            self.timmy_the_turtle.forward(10)
        print(output)

    def spirograph(self, radius, number_of_circle):
        self.timmy_the_turtle.speed(20)
        size_of_angle = float(360 / number_of_circle)
        for n in range(number_of_circle):
            self.random_color()
            self.timmy_the_turtle.circle(radius)
            self.timmy_the_turtle.rt(size_of_angle)

    def hirst_painting(self, number_of_dots):
        self.timmy_the_turtle.penup()
        self.timmy_the_turtle.rt(135)
        self.timmy_the_turtle.forward(number_of_dots * 50 / 2)
        self.timmy_the_turtle.lt(135)
        x = self.timmy_the_turtle.pos()
        y = x[1]
        for n in range(0, number_of_dots):
            for m in range(0, number_of_dots):
                self.random_color_dot(20)
                self.timmy_the_turtle.forward(50)
            y += 50
            self.timmy_the_turtle.setpos(x[0], y)
