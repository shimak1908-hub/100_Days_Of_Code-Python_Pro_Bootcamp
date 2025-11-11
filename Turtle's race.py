import random
from turtle import Turtle , Screen

screen = Screen()

screen.setup(500 , 500)
name = screen.textinput(title="Bet on a turtle" , prompt="Enter the colour of the turtle ")
colors = ("red" , "blue" , "orange" , "yellow" , "purple")
y_pos = (100 , 50 , 0 , -50 , -100)
new_turtles = []
for turtle_racers in range(0,5):
    tim = Turtle()
    tim.shape("turtle")
    tim.penup()
    tim.color(colors[turtle_racers])
    tim.goto(x = -230 ,  y = (y_pos[turtle_racers]) )
    new_turtles.append(tim)
bro = True
while bro:
    for turtle in new_turtles:
        if turtle.xcor() >230:
            bro = False
            winning_color = turtle.pencolor()
            if winning_color == name:
                print(f"You won! The {winning_color} turtle is the winnner!")
            else:
                print(f"You lost! The {winning_color} turtle is the winnner!")
        magga = random.randint(1,10)
        turtle.forward(magga)





print(new_turtles)
screen.exitonclick()