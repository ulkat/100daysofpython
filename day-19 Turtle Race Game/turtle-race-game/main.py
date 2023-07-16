from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which Turtle will win the race ? Choose a color:")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []

for i in range(len(colors)):
    turtle_list.append(Turtle(shape="turtle"))
    turtle_list[i].color(colors[i])
    turtle_list[i].penup()
    turtle_list[i].goto(x=-230, y=-90 + (i * 30))
    turtle_list[i].speed("fastest")
if user_bet:
    is_race_on = True


while is_race_on == True :
    for turtle in turtle_list:
        if  turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet :
                print(f"You've won, the winning color is {winning_color}.")

            else :
                print(f"You've lost, the winning color is {winning_color}.")

        random_distance = random.randint(1,10)
        turtle.forward(random_distance)







screen.exitonclick()