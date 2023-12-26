from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
NUMBER_OF_CAR = 20


class CarManager:

    def __init__(self):
        self.garage = []
        self.level = 1
        self.set_the_car()

    def generate_car(self):
        """ 장애물 초기 설정 및 단일 객체 생성"""
        new_car = Turtle()
        new_car.shape('square')
        new_car.shapesize(stretch_wid=1, stretch_len=3)
        new_car.penup()
        color_for_car = COLORS[randint(0, 5)]
        new_car.color(color_for_car)
        new_x = randint(-300, 600)
        new_y = [-240, -220, -200, -180, -160, -140, -120, -100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100, 120,
                 140, 160, 180, 200, 220, 240]
        new_car.goto(new_x, new_y[randint(0, len(new_y) - 1)])
        self.garage.append(new_car)

    def set_the_car(self):
        """ 객체 수 설정 및 생성 """
        for n in range(NUMBER_OF_CAR - 1):
            self.generate_car()

    def move_car(self):
        for car in self.garage:
            new_x = car.xcor()
            new_x -= STARTING_MOVE_DISTANCE
            if self.level >= 2:
                new_x -= (MOVE_INCREMENT * self.level - 1) + STARTING_MOVE_DISTANCE
            car.goto(new_x, car.ycor())
            if new_x <= -310:
                new_x = car.xcor() + 610
                car.goto(new_x, car.ycor())
