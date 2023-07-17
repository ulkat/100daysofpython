from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1, )
        self.color("white")
        self.penup()
        self.speed("normal")
        self.coordinates = coordinates
        self.goto(coordinates)

    def paddle_up(self):
        y_cor = self.ycor() + 20
        self.goto(self.xcor(), y_cor)

    def paddle_down(self):
        y_cor = self.ycor() - 20
        self.goto(self.xcor(), y_cor)
