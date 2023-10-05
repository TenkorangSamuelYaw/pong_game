# First created by Allan Alcorn.
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

BACKGROUND_COLOR = "black"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TITLE = "PONG GAME"

screen = Screen()
screen.bgcolor(BACKGROUND_COLOR)
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title(TITLE)
screen.tracer(0)
#  Create an instance of the various class.
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()  # Start listening for keystrokes.
screen.onkey(key="Up", fun=right_paddle.up)
screen.onkey(key="Down", fun=right_paddle.down)
screen.onkey(key="w", fun=left_paddle.up)
screen.onkey(key="s", fun=left_paddle.down)

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    #  Detect collision with top and bottom wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #  Detect collision with both paddles.
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    #  Detect when right paddle misses. (Paddle is from 340 to 360)
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()  # Player on the left scores by 1
    #  Detect when left paddle misses.
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()  # Player on the right scores by 1

screen.exitonclick()
