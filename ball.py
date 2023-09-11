from turtle import Turtle, Screen
import random
import colorsys

screen = Screen()
screen.colormode(255)


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.reset_position()
        self.step_y = 15
        self.step_x = 15
        self.move_speed = 0.1

    def reset_position(self):
        self.setposition(0, -279)
        self.set_color()
        self.move_speed = 0.1

    def set_color(self):
        h, s, l = random.random(), 0.5 + random.random() / 2.0, 0.4 + random.random() / 5.0
        r, g, b = [int(256 * i) for i in colorsys.hls_to_rgb(h, l, s)]
        self.color(r, g, b)

    def move(self):
        x = self.xcor() + self.step_x
        y = self.ycor() + self.step_y
        self.setposition(x, y)

    def bounce_wall(self):
        self.step_x *= -1

    def bounce_ceiling(self):
        self.step_y *= -1

    def bounce_paddle(self):
        self.step_y *= -1
        self.move_speed *= 0.99
