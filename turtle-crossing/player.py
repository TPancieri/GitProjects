from turtle import Turtle
MOVEMENT = 10


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.setheading(90)
        self.start_point()

    def move(self):
        self.forward(MOVEMENT)

    def start_point(self):
        self.goto(0, -260)
