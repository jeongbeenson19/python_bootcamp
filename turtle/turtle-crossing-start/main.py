import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

user = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(user.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.score()
    cars.move_car()

    # 충돌 감지
    for car in cars.garage:
        if user.distance(car) <= 40 and user.ycor() - car.ycor() < 9:
            game_is_on = False
            scoreboard.game_over()

    # 난이도 상승 여부 감지
    if user.ycor() > 320:
        user.__init__()
        cars.level += 1
        scoreboard.level += 1
        scoreboard.score()

screen.exitonclick()
