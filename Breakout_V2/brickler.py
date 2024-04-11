import turtle
from brick import Brick


class Brickler:
    def __init__(self, screenwidth, screenheight):
        brickwidth = 40
        brickheight = 20
        h_spacing = 5
        v_spacing = 5
        num_rows = 4

        width = round(screenwidth / 2)
        height = round(screenheight / 2)

        self.bricks = []

        total_brick_height = num_rows * brickheight
        total_v_spacing = v_spacing * (num_rows - 1)

        for y in range(height - total_brick_height - total_v_spacing, height,
                       brickheight + v_spacing):
            for x in range(-width + round(brickwidth / 2) + h_spacing + 5, width - round(brickwidth / 2) - h_spacing, brickwidth + h_spacing):
                new_brick = Brick()
                new_brick.goto(x, y)
                self.bricks.append(new_brick)

    def cleanup(self):
        for b in self.bricks:
            if b.hit:
                b.hideturtle()
                self.bricks.remove(b)