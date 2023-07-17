from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()

screen.onkey(r_paddle.paddle_up, "Up")
screen.onkey(r_paddle.paddle_down, "Down")
screen.onkey(l_paddle.paddle_up, "w")
screen.onkey(l_paddle.paddle_down, "s")


game_is_on = True
timer = 0.1

while game_is_on:
    time.sleep(timer)
    screen.update()
    ball.move()

# detext collision with the walls

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

# detect collusion with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        timer *= 0.9

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_score_up()
        timer = 0.1

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_score_up()
        timer = 0.1

screen.exitonclick()
