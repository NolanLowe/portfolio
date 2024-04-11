from object import Object

class Brick(Object):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2, 1)
        self.update()
        self.hit = False

    def flag(self):
        self.hit = True