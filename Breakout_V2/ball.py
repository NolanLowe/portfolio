from object import Object
import time

class Ball(Object):
    vertical_axes = ["y", 't', 'b']
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.update()

    def rebound(self, axis):
        if axis in Ball.vertical_axes:
            self.setheading(360 - self.heading())
        else:
            self.setheading(180 - self.heading())

    def angled_shot(self, offset):
        self.setheading(self.heading() - offset)