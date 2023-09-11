from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)


class BricksManager:

    def __init__(self):
        self.bricks = []

    def create_bricks(self):
        for x in range(0, 5):
            for y in range(0, 8):
                new_brick = Turtle("square")
                new_brick.penup()
                r = int(random.randint(100, 200))
                g = int(random.randint(100, 200))
                b = int(random.randint(100, 200))
                new_brick.color(r, g, b)
                new_brick.shapesize(stretch_wid=1, stretch_len=4.7)
                new_brick.setposition((x*100 - 204), (y*25 + 100))
                self.bricks.append(new_brick)
