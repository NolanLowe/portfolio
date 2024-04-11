from object import Object
import time

class Ball(Object):
    vertical_axes = ["y", 't', 'b']
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.update()
        self.off_paddle = False
        self.offset = 0

    def rebound(self, axis):
        if axis in Ball.vertical_axes:
            self.setheading(360 - self.heading())
            thread = self.get_thread(self.jiggle, stretch_x=1.2, stretch_y=0.8)
            thread.start()
        else:
            self.setheading(180 - self.heading())
            thread = self.get_thread(self.jiggle, stretch_x=0.8, stretch_y=1.2)
            thread.start()

        if self.off_paddle:
            self.angled_shot()

    def angled_shot(self):
        self.setheading(self.heading() + self.offset)
        self.off_paddle = False
        self.offset = 0

    def jiggle(self, stretch_x, stretch_y):
        # turtle.turtlesize(Y, X, outline)
        self.shapesize(stretch_y, stretch_x)
        time.sleep(0.08)
        self.shapesize(1, 1)
        return