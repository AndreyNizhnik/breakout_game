from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, z):
        super().__init__()
        self.shape("square")
        self.color("light gray")
        self.shapesize(stretch_wid=1, stretch_len=6)
        self.penup()
        self.setposition(z)

    def move_left(self):
        new_x = self.xcor() - 20
        new_y = self.ycor()
        self.goto(new_x, new_y)

    def move_right(self):
        new_x = self.xcor() + 20
        new_y = self.ycor()
        self.goto(new_x, new_y)
