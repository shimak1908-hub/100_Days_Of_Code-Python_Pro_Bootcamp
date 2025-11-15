from turtle import Turtle , Screen
from paddle_class import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


ping = Turtle()
pong = Turtle()
screen = Screen()
scoreboard = Scoreboard()



screen.setup(800 , 600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350 , 0))
l_paddle = Paddle((-350 , 0))
ball = Ball()


screen.listen()
screen.onkey(l_paddle.go_up , "w")
screen.onkey(l_paddle.go_down , "s")
screen.onkey(r_paddle.go_up , "Up")
screen.onkey(r_paddle.go_down , "Down")


game_is_on = True
while game_is_on:

    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
        ball.left_bounce()
        scoreboard.increase_r_score()
    if ball.distance(l_paddle) < 50 and ball.xcor() < -340 :
        ball.left_bounce()
        scoreboard.increase_l_score()
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.reset()
        ball.left_bounce()
screen.exitonclick()