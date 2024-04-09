from collideable import Collideable


class Brick(Collideable):

    def __init__(self, height=1, width=2, border=1):
        super().__init__()

        self.shape("square")
        self.shapesize(height, width, border)
        self.update()
        self.is_brick = True
