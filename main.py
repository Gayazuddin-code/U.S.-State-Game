import turtle
from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("U.S. States Game")
image = "states.gif"
screen.register_shape(image)
turtle.shape(image)
count = 0
correct_states = []
while True:
    answer_state = screen.textinput(title=f"{count}/50 U.S. State Game", prompt="What's State name?")
    answer_state = answer_state.title()
    data = pandas.read_csv("50_states.csv")
    row = data[data.state == answer_state]
    states = data.state.to_list()
    if answer_state in states:
        count += 1
        coordinates = []
        x = row.x
        x = x.to_list()
        coordinates.append(x[0])
        y = row.y
        y = y.to_list()
        coordinates.append(y[0])
        tim = Turtle()
        tim.penup()
        tim.goto(coordinates[0], coordinates[1])
        tim.pendown()
        tim.write(answer_state)

turtle.mainloop()
