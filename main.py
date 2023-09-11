from turtle import Screen
import time
from paddle import Paddle
from bricks_manager import BricksManager
from scoreboard import Scoreboard
from win import Win
from gameover import GameOver
from ball import Ball

# Set up Screen
screen = Screen()
screen.setup(width=500, height=700)
screen.bgcolor("black")
screen.title("Breakout Game v1.1.0")
screen.tracer(0)
screen.colormode(255)

# Set up Paddle
paddle = Paddle((0, -300))
screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")
screen.update()

# Set up Bricks
bricks_manager = BricksManager()
bricks_manager.create_bricks()
screen.update()

# Set up Ball
ball = Ball()
screen.update()

# Set up ScoreBoard
scoreboard = Scoreboard()
screen.update()

def game():
    game_over = False
    while not game_over:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        # ball hits the wall
        if ball.xcor() > 225 or ball.xcor() < -230:
            ball.bounce_wall()

        # ball hits the ceiling
        if ball.ycor() > 330:
            ball.bounce_ceiling()

        # ball hits the floor (Game Over)
        if ball.ycor() < -360:
            game_over = True
            GameOver()

        # ball hits the paddle (+speed increase)
        if ball.ycor() < -270 and ball.distance(paddle) < 40:
            ball.bounce_paddle()

        # ball hits the brick
        for brick in bricks_manager.bricks:
            if ball.distance(brick) < 30:
                ball.bounce_ceiling()
                bricks_manager.bricks.remove(brick)
                brick.color(0, 0, 0)
                scoreboard.update_scoreboard()

        # check if won
        if len(bricks_manager.bricks) == 0:
            for brick in bricks_manager.bricks:
                brick.color(0, 0, 0)
            game_over = True
            Win()


# Start the game cycle
screen.onkey(game, "space")

# Keep window open
screen.exitonclick()
