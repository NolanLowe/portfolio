import time

from paddle import Paddle
from ball import Ball
from brick import Brick
from turtle import *
import random


class Game:

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
        self.ball = [Ball(self.collideables, self.paddle)]
        self.ball[0].goto(self.ball_start_pos)
        self.ball[0].setheading(70)

        self.spawn_additional_ball()

        self.run()
        self.screen.mainloop()


    def run(self):
        self.paddle.move()
        if not self.ball[0].move():
            self.reset_ball()
        if (len(self.ball) > 1):
            for ball in self.ball[1:]:
                ball.move()
        self.screen.update()
        self.screen.ontimer(self.run, 10)

    def spawn_additional_ball(self):
        new_ball = Ball(self.collideables, self.paddle)
        new_ball.setheading(random.randint(60, 80))
        self.ball.append(new_ball)


    def reset_ball(self):
        self.ball[0].goto(self.ball_start_pos)
        self.ball[0].setheading(70)