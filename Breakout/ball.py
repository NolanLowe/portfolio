from collideable import Collideable
from brick import Brick
from paddle import Paddle
import random


class Ball(Collideable):
    def __init__(self, collideables, paddle):
        super().__init__()
        self.shape("circle")
        self.collideables: list[Collideable] = collideables
        self.update()
        self.movespeed = 10
        self.paddle = paddle


    def move(self):
        in_bounds, axis = self.in_bounds(self.movespeed)
        if in_bounds:
            for item in self.collideables:
                collided, axis = self.collision(item)
                if collided:

                    if isinstance(item, Brick):
                        item.hideturtle()
                        self.collideables.remove(item)
                        del item

                    if axis == "y":
                        heading = 360 - self.heading()
                        if self.paddle.moving_left:
                            heading += round(random.random() * 20)
                        elif self.paddle.moving_right:
                            heading -= round(random.random() * 20)
                        self.setheading(heading)
                        self.move()
                    else:
                        print("x axis collision w/spacer")
                        heading = 180 - self.heading()
                        self.setheading(heading)
                        self.move()

            # no collisions with objects, and still in bounds, go ahead and move.
            self.forward(self.movespeed)

        # ball is going out of bounds - ie hit edge of screen
        # rebound if any wall but the bottom
        else:
            if axis == "y":
                if self.ycor() < 0:
                    # goes out of bounds:
                    self.destroy()
                    return False
                heading = 360 - self.heading()
                self.setheading(heading)
                self.move()
            else:
                heading = 180 - self.heading()
                self.setheading(heading)
                self.move()
        return True


    def destroy(self):
        pass
