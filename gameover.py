from turtle import Turtle
import random


class GameOver(Turtle):

    def __init__(self):
        super().__init__()
        red = int(random.randint(100, 255))
        green = int(random.randint(100, 255))
        blue = int(random.randint(100, 255))
        self.color(red, green, blue)
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=("Broadway", 50, "normal"))
