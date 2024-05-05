from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.setpos(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.velocity = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # invert y
        self.y_move *= -1
        # increase velocity
        self.velocity *= 0.9

    def bounce_x(self):
        # invert x
        self.x_move *= -1
        # increase velocity
        self.velocity *= 0.9

    def reset(self):
        self.clear()
        self.home()
        self.bounce_x()
        self.velocity = 0.1
