from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
ball = Ball()
scoreboard = Scoreboard()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

game = True
while game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # detect Collision with wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()
    # detect Collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    # when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
screen.exitonclick()
