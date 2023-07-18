import turtle
import pandas
import time

screen = turtle.Screen()
screen.title("U.S. Statetes Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

data = pandas.read_csv("50_states.csv")

state_list = data.state

guessed_states = []


while len(guessed_states) < 50:
    time.sleep(0.1)
    screen.update()
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's the another state name").title()
    if answer_state == "Exit":
        # states to learn.csv with list comprehension
        states_to_learn = [state for state in state_list if state not in guessed_states]
        states_to_learn_data = pandas.DataFrame(states_to_learn)
        states_to_learn_data.to_csv("states_to_learn_data")
        break

    for state in state_list:
        if answer_state == state:
            new_row = data[data["state"] == state]
            x = int(new_row.x)
            y = int(new_row.y)
            new_turtle = turtle.Turtle()
            new_turtle.hideturtle()
            new_turtle.penup()
            new_turtle.goto(x, y)
            new_turtle.write(state, align="center",)
            guessed_states.append(state)

#states to learn.csv










