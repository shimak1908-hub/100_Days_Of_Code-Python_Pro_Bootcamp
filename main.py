import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

IMAGE = "blank_states_img.gif"
screen.addshape(IMAGE)
turtle.shape(IMAGE)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="Write the name of a U.S. state (or type Exit):"
    )

    if answer_state is None:
        continue

    answer_state = answer_state.title()

    if answer_state == "Exit":
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)

        state_data = data[data.state == answer_state]

        marker = turtle.Turtle()
        marker.hideturtle()
        marker.penup()
        marker.goto(state_data.x.item(),state_data.y.item())
        marker.write(answer_state, align="center", font=("Arial", 10, "normal"))


missing_states = [state for state in all_states if state not in guessed_states]

pd.DataFrame(missing_states).to_csv("states_to_learn.csv", index=False)

turtle.mainloop()


screen.exitonclick()