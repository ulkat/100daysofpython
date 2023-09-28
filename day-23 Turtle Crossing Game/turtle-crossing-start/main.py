import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


turtle = Player()
car_manager = CarManager()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(turtle.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    if turtle.ycor() > 290:
        turtle.reset_position()
        car_manager.level_up()
        scoreboard.score_up()

    for car in car_manager.cars:
       if car.distance(turtle) < 20:
           game_is_on = False
           scoreboard.game_over()


screen.exitonclick()