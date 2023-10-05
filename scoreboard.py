from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=-100, y=200)  # For the left score.
        self.write(f"{self.l_score}", align="center", font=("Courier", 80, "normal"))
        self.goto(x=100, y=200)  # For the right score.
        self.write(f"{self.l_score}", align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
