from turtle import Screen
from paddle import Paddle
from ball import Ball
from computer import Computer
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=900, height=600)
screen.title('Pong game')
screen.tracer(0)

paddle = Paddle((-430, 0))
computer = Computer((430, 0))
pong_ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.go_up, "Up")
screen.onkey(paddle.go_down, "Down")

game_is_on = True
period_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.01)
    screen.update()
    pong_ball.move()

    # 유저 패들과 공 접촉 감지
    if (pong_ball.distance(paddle) <= 50 and pong_ball.xcor() < -420) or (pong_ball.distance(computer) <= 50 and
                                                                          pong_ball.xcor() > 420):
        pong_ball.x_bounce()

    # 공과 x축 벽 접촉 감지
    if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
        pong_ball.y_bounce()

    # 컴퓨터 패들 자동 조작
    if pong_ball.xcor() > 0 and pong_ball.ycor() > computer.ycor():
        computer.c_up()

    if pong_ball.xcor() > 0 and pong_ball.ycor() < computer.ycor():
        computer.c_down()

    if pong_ball.xcor() > 470:
        scoreboard.user_get_score()
        pong_ball.__init__()

    elif pong_ball.xcor() < -470:
        scoreboard.computer_get_score()
        pong_ball.__init__()

    # 공과 y축 벽 접촉 감지

screen.exitonclick()
