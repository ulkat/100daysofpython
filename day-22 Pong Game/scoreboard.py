from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 200)
        self.write(self.l_score, align="left", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="right", font=("Courier", 80, "normal"))

    def r_score_up(self):
        self.clear()
        self.r_score += 1
        self.update_scoreboard()

    def l_score_up(self):
        self.clear()
        self.l_score += 1
        self.update_scoreboard()
