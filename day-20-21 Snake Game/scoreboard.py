from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-10, 260)
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.write(f"Score:{str(self.score)}", False, "center", font=('Courier', 30, 'normal'))



    def score_up(self):
        self.clear()
        self.score += 1
        self.write(f"Score:{str(self.score)}", False, "center", font=('Courier', 30, 'normal'))


    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, "center", font=('Courier', 30, 'normal'))






