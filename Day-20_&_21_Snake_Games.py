from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

def go_up():
    if snake.head.heading() != 270:
        snake.head.setheading(90)

def go_down():
    if snake.head.heading() != 90:
        snake.head.setheading(270)

def go_left():
    if snake.head.heading() != 0:
        snake.head.setheading(180)

def go_right():
    if snake.head.heading() != 180:
        snake.head.setheading(0)

screen.listen()
screen.onkey(go_up, "w")
screen.onkey(go_down, "s")
screen.onkey(go_left, "a")
screen.onkey(go_right, "d")

game_playing = True
while game_playing:
    screen.update()
    time.sleep(0.1)
    snake.move()


    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_scoreboard()


    if (snake.head.xcor() > 280 or snake.head.xcor() < -300 or
        snake.head.ycor() > 280 or snake.head.ycor() < -300):
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:  # skip the head
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
screen.exitonclick()
