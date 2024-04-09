from collideable import Collideable


class Paddle(Collideable):
    movespeed = 8
    def __init__(self):
        super().__init__()
        self.moving_left = False
        self.moving_right = False

        self.shape("square")
        self.shapesize(1, 4, 1)
        self.movespeed = 10
        self.update()

    def move(self):
        if self.moving_left:
            self.setheading(180)
            if self.in_bounds(Paddle.movespeed):
                self.forward(Paddle.movespeed)
        elif self.moving_right:
            self.setheading(0)
            if self.in_bounds(Paddle.movespeed):
                self.forward(Paddle.movespeed)

    def start_left(self):
        self.moving_left = True
    def stop_left(self):
        self.moving_left = False
    def start_right(self):
        self.moving_right = True
    def stop_right(self):
        self.moving_right = False