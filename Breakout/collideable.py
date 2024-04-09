from turtle import Turtle


class Collideable(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.movespeed = None
        self.is_brick = False

        screen = self.screen
        self.max_x = screen.window_width() / 2
        self.mix_x = -screen.window_width() / 2
        self.max_y = screen.window_height() / 2
        self.min_y = -screen.window_height() / 2

        # shapesize = (Height, Width, Border)
        self.width = self.shapesize()[1] * 10
        self.height = self.shapesize()[0] * 10

    def collision(self, obj):
        old_position = self.pos()
        self.forward(self.movespeed)

        if abs(self.xcor() - obj.xcor()) <= (self.width + obj.width):
            if abs(self.ycor() - obj.ycor()) <= (self.height + obj.height):
                axis = self.collision_axis(obj)
                self.goto(old_position)
                return True, axis

        self.goto(old_position)
        return False, None

    def collision_axis(self, obj):
        if obj.xcor() - obj.width< self.xcor() < obj.xcor() + obj.width:
            return "y"
        else:
            return "y"

    def in_bounds(self, units):
        oldpos = self.pos()

        self.forward(units)

        inbounds_x = self.mix_x + self.width < self.xcor() < self.max_x - self.width
        inbounds_y = self.min_y + self.height < self.ycor() < self.max_y - self.height

        self.goto(oldpos)

        if inbounds_y and inbounds_x:
            return True, None

        # if not inbounds_x and not inbounds_y:
        #     return False, "xy"
        if not inbounds_x:
            return False, "x"
        elif not inbounds_y:
            return False, "y"

    def update(self):
        screen = self.screen
        self.max_x = screen.window_width() / 2
        self.mix_x = -screen.window_width() / 2
        self.max_y = screen.window_height() / 2
        self.min_y = -screen.window_height() / 2

        # shapesize = (Height, Width, Border)
        self.width = self.shapesize()[1] * 10
        self.height = self.shapesize()[0] * 10