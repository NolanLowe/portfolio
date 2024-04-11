import turtle
from object import Object
from paddle import Paddle
from ball import Ball
from brickler import Brickler
from brick import Brick

prev_pos = None
sep_x, sep_y, size_x, size_y = 0, 0, 0, 0
o1l, o1r, o1t, o1b = 0, 0, 0, 0
o2l, o2r, o2t, o2b = 0, 0, 0, 0


class ObjectHandler:
    left_bounds = None
    right_bounds = None
    top_bounds = None
    bottom_bounds = None

    def __init__(self, screen):
        self.ball_speed = 10
        self.paddle_speed = 8

        self.screen = screen
        self.screen.tracer(False)
        self.screen.bgcolor("black")
        self.screen.setup(width=520, height=660)
        self.screen.onkeypress(self.paddle_start_left, 'Left')
        self.screen.onkeypress(self.paddle_start_right, 'Right')
        self.screen.onkeyrelease(self.paddle_stop_left, 'Left')
        self.screen.onkeyrelease(self.paddle_stop_right, 'Right')

        ObjectHandler.left_bounds = -screen.window_width() / 2
        ObjectHandler.right_bounds = screen.window_width() / 2
        ObjectHandler.top_bounds = screen.window_height() / 2
        ObjectHandler.bottom_bounds = -screen.window_height() / 2

        self.paddle = Paddle()
        self.paddle.goto(0, -240)

        self.ball = Ball()
        self.ball.setheading(70)

        self.paddle_moving_left = False
        self.paddle_moving_right = False

        self.screen.listen()
        self.brickler = Brickler(520, 660)

        self.run()
        self.screen.mainloop()

    def run(self):
        self.move_paddle()
        self.legalize_move(self.ball, self.ball_speed)
        self.brickler.cleanup()
        self.screen.update()
        self.screen.ontimer(self.run, 10)

    def in_bounds(self, obj: Object):
        if not self.get_edge(obj, 'b') > self.bottom_bounds:
            return False, 'b'

        if not self.get_edge(obj, 't') < self.top_bounds:
            return False, 't'

        if not self.get_edge(obj, 'l') > self.left_bounds:
            return False, 'l'

        if not self.get_edge(obj, 'r') < self.right_bounds:
            return False, 'r'

        return True, None

    def get_edge(self, obj: Object, edge):
        """
        return x or y cordinate corresponding to parameter edge
        ie 'l' == left -> will return the X coordinate of the leftmost edge of the object
        :param obj:
        :param edge: selection from ['l', 'r', 'u', 'b']
        :return:
        """
        # turtle.turtlesize(Y, X, outline)
        match edge:
            case 'l':
                return obj.xcor() - obj.width / 2
            case 'r':
                return obj.xcor() + obj.width / 2
            case 't':
                return obj.ycor() + obj.height / 2
            case 'b':
                return obj.ycor() - obj.height / 2
            case default:
                return "Invalid selection"

    def collided(self, obj1: Object, obj2: Object):
        global sep_x, sep_y, size_x, size_y
        """
        check if two objects have overlapped.
        :param obj1:
        :param obj2:
        :return:
        """
        sep_x = abs(obj1.xcor() - obj2.xcor())
        sep_y = abs(obj1.ycor() - obj2.ycor())

        size_x = obj1.width / 2 + obj2.width / 2
        size_y = obj1.height / 2 + obj2.height / 2

        if sep_x > size_x or sep_y > size_y:
            return False
        else:
            if isinstance(obj2, Brick):
                obj2.flag()
            elif isinstance(obj1, Brick):
                obj1.flag()
            return True

    def are_touching(self, obj1: Object, obj2: Object):
        global o1l, o1r, o1t, o1b, o2l, o2r, o2t, o2b
        o1l = self.get_edge(obj1, 'l')
        o1r = self.get_edge(obj1, 'r')
        o1t = self.get_edge(obj1, 't')
        o1b = self.get_edge(obj1, 'b')
        o2l = self.get_edge(obj2, 'l')
        o2r = self.get_edge(obj2, 'r')
        o2t = self.get_edge(obj2, 't')
        o2b = self.get_edge(obj2, 'b')
        """
        checks if two objects are in close enough proximity to be considered 'touching'
        :param obj1:
        :param obj2:
        :return: [axis], [coordinate] or None None if not touching
        """
        if abs(o1l - o2r) < 3:
            return "x", o1l
        elif abs(o1r - o2l) < 3:
            return 'x', o1r
        elif abs(o1t - o2b) < 3:
            return 'y', o1t
        elif abs(o1b - o2t) < 3:
            return 'y', o1b

        return False, None

    def is_legal(self, obj: Object):
        """
        check if obj has collided with any others, and is still in bounds
        :param obj:
        :return:
        """
        inbounds, axis = self.in_bounds(obj)
        if not inbounds:
            return False, axis

        if isinstance(obj, Ball):
            if self.collided(obj, self.paddle):
                edge, value = self.are_touching(obj, self.paddle)
                return False, edge
            for item in self.brickler.bricks:
                if self.collided(obj, item):
                    edge, value = self.are_touching(obj, item)
                    return False, edge

        return True, None


    def legalize_move(self, obj: Object, distance: int, previous_axis=None):
        global prev_pos
        """
        moves object forward in existing heading by [distance] units
        in the event that the full distance results in a collision or OOB,
        will move the most that it can, or None if touching obj or already in illegal placement.
        :param obj:
        :param distance:
        :return:
        """
        prev_pos = obj.pos()
        obj.forward(distance)

        legal, axis = self.is_legal(obj)
        obj.goto(prev_pos)

        if not legal:
            self.legalize_move(obj, distance - 1, axis)
            return

        obj.forward(distance)

        if isinstance(obj, Ball) and distance < self.ball_speed:
            obj.rebound(previous_axis)
            obj.forward(self.ball_speed - distance)

    def move_paddle(self):
        if self.paddle_moving_left or self.paddle_moving_right:
            self.legalize_move(self.paddle, self.paddle_speed)

    def paddle_start_left(self):
        self.paddle_moving_left = True
        self.paddle.setheading(180)

    def paddle_stop_left(self):
        self.paddle_moving_left = False

    def paddle_start_right(self):
        self.paddle_moving_right = True
        self.paddle.setheading(0)

    def paddle_stop_right(self):
        self.paddle_moving_right = False
