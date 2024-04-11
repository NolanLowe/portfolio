import turtle
import threading



class Object(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.width = None
        self.height = None

    def update(self):
        self.width = self.__get_width()
        self.height = self.__get_height()

    def __get_width(self):
        # turtle.turtlesize(Y, X, outline)
        return self.shapesize()[1] * 20

    def __get_height(self):
        return self.shapesize()[0] * 20

    def get_thread(self, function, **kwargs):
        thread = threading.Thread(target=function, daemon=True, kwargs=kwargs)
        return thread
