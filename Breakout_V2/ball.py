from object import Object


class Ball(Object):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.update()

    def rebound(self, axis):
        if axis in ["y", 't', 'b']:
            heading = 360 - self.heading()
            self.setheading(heading)
        else:
            heading = 180 - self.heading()
            self.setheading(heading)
