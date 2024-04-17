from object import Object
import time


class Paddle(Object):
    movespeed = 8
    def __init__(self):
        super().__init__()
        self.moving_left = False
        self.moving_right = False

        self.shape("square")
        self.shapesize(1, 4, 1)
        self.movespeed = 10
        self.update()