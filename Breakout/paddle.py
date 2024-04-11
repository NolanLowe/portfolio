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
        inbounds, axis = self.in_bounds(Paddle.movespeed)
        if self.moving_left:
            if inbounds:
                self.forward(Paddle.movespeed)
        elif self.moving_right:
            if inbounds:
                self.forward(Paddle.movespeed)

    def start_left(self):
        self.moving_left = True
        self.setheading(180)
    def stop_left(self):
        self.moving_left = False
    def start_right(self):
        self.moving_right = True
        self.setheading(0)
    def stop_right(self):
        self.moving_right = False