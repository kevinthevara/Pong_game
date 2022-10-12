from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("PONG")

screen.tracer(0)

scoreboard = Scoreboard()
scoreboard.update(0, 0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

ball = Ball()


r_paddle.move(0)
l_paddle.move(2)

game_on = True

while game_on:
    time.sleep(ball.move_flash)
    screen.update()
    ball.move_up()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    if ball.xcor() >= 340 and ball.distance(r_paddle) < 50:
        ball.bounce_x()

    if ball.xcor() <= -340 and ball.distance(l_paddle) < 50:
        ball.bounce_x()



    if ball.xcor() > 390:
        ball.start_position()
        ball.bounce_x()
        scoreboard.update(1, 0)

    if ball.xcor() < -390:
        ball.start_position()
        ball.bounce_x()
        scoreboard.update(0, 1)

    if scoreboard.l_points == 10 :
        game_on = False
        print(f"Congratulations to player 1!")
    elif scoreboard.r_points == 10:
        game_on = False
        print(f"Congratulations to player 2!")


screen.exitonclick()
