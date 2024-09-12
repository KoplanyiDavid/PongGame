from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# Create screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Create the paddles
right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)

# Create the ball
ball = Ball()

# Create scoreboard
scoreboard = Scoreboard()

# Setup listeners
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 330 or ball.distance(left_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # Detect when ball goes out
    if ball.xcor() > 390:
        ball.reset_position()
        ball.increase_speed()
        scoreboard.l_point()

    if ball.xcor() < -390:
        ball.reset_position()
        ball.increase_speed()
        scoreboard.r_point()

screen.exitonclick()
