from collideable import Collideable
from brick import Brick


class Ball(Collideable):
    def __init__(self, collideables):
        super().__init__()
        self.shape("circle")
        self.collideables: list[Collideable] = collideables
        self.update()
        self.movespeed = 10


    def move(self):
        in_bounds, axis = self.in_bounds(self.movespeed)
        if in_bounds:
            for item in self.collideables:
                collided, axis = self.collision(item)
                if collided:
                    print("collision detected")
                    if item.is_brick:
                        print("collision with Brick!")
                        item.hideturtle()
                        self.collideables.remove(item)
                        del item
                    else:
                        print("collision with non-brick")
                    if axis == "y":
                        heading = 360 - self.heading()
                        self.setheading(heading)
                        self.move()
                    else:
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
