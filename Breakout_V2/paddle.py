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

    def jiggle(self):
        thread = self.get_thread(self.__jiggle)
        thread.start()

    def __jiggle(self):
        # turtle.turtlesize(Y, X, outline)
        self.shapesize(0.8, 4.2)
        time.sleep(0.06)
        self.shapesize(1.2, 3.8)
        time.sleep(0.04)
        self.shapesize(1, 4)
        return
