import turtle
import threading
import time


class Object(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.width = None
        self.height = None
        self.shapeheight = None
        self.shapewidth = None

    def update(self):
        self.width = self.shapesize()[1] * 20
        self.height = self.shapesize()[0] * 20
        self.shapeheight = self.shapesize()[0]
        self.shapewidth = self.shapesize()[1]

    def get_thread(self, function, **kwargs):
        thread = threading.Thread(target=function, daemon=True, kwargs=kwargs)
        return thread

    def jiggle(self):
        thread = self.get_thread(self.__jiggle)
        thread.start()

    def __jiggle(self):
        # turtle.turtlesize(Y, X, outline)
        self.shapesize(0.8 * self.shapeheight, 1.2 * self.shapewidth)
        time.sleep(0.04)
        self.shapesize(1.05 * self.shapeheight, 0.95 * self.shapewidth)
        time.sleep(0.04)
        self.shapesize(self.shapeheight, self.shapewidth)
