import turtle
from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("U.S. States Game")
image = "states.gif"
screen.register_shape(image)
turtle.shape(image)
tim = Turtle()
tim.hideturtle()
correct_states = []
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
while len(correct_states) < 50:
    answer_state = screen.textinput(title=f"{len(correct_states)}/50 Correct States",
                                    prompt="What's State name?").title()
    row = data[data.state == answer_state]
    if answer_state == "Exit":
        break
    if answer_state in states:
        correct_states.append(answer_state)
        states.remove(answer_state)
        tim.penup()
        tim.goto(int(row.x), int(row.y))
        tim.pendown()
        tim.write(answer_state)

new_data = pandas.DataFrame(states)
new_data.to_csv("state_to_learn.csv")
