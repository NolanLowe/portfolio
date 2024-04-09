import time

from paddle import Paddle
from ball import Ball
from brick import Brick
from turtle import *


class Game:
    framerate = 1 / 60

    def __init__(self, width=520, height=660):
        self.screen = Screen()
        self.screen.tracer(False)
        self.screen.bgcolor("black")
        self.screen.setup(width=width, height=height)

        self.ball_start_pos = (0, 0)
        self.paddle_start_pos = (0, -height / 3)

        self.paddle = Paddle()
        self.paddle.goto(self.paddle_start_pos)

        self.screen.onkeypress(self.paddle.start_left, 'Left')
        self.screen.onkeypress(self.paddle.start_right, 'Right')
        self.screen.onkeyrelease(self.paddle.stop_left, 'Left')
        self.screen.onkeyrelease(self.paddle.stop_right, 'Right')

        self.screen.listen()
        self.collideables = [self.paddle]

        brick = Brick()
        brick.hideturtle()
        for y in range(round(height/4), round(height/2), brick.height * 2 + 5):
            for x in range(round(-width/2) + brick.width + 10, round(width/2) - brick.width, brick.width * 2 + 5):
                new_brick = Brick()
                new_brick.teleport(x, y)
                self.collideables.append(new_brick)
        del brick


        # self.screen.onkey()
        ball = Ball(self.collideables)
        ball.goto(self.ball_start_pos)
        ball.setheading(70)

        while True:
            time.sleep(Game.framerate)
            self.paddle.move()
            if not ball.move():
                ball = self.reset_ball(ball)
            self.screen.update()



    def reset_ball(self, b):
        b.hideturtle()
        del b
        ball = Ball(self.collideables)
        ball.goto(self.ball_start_pos)
        ball.setheading(70)
        return ball