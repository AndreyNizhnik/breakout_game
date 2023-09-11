from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("light gray")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 300)
        self.write(f"Score: {self.score}", align="center", font=("Broadway", 30, "normal"))
        self.score += 10
