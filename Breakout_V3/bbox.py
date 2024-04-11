from turtle import Turtle
class BBox():
    def __init__(self, obj: Turtle):
        # turtle.turtlesize(Y, X, outline)
        self.width = obj.shapesize()[1] * 20
        self.height = obj.shapesize()[0] * 20
        self.left = obj.xcor()
        self.right = None
        self.top = None
        self.bottom = None



