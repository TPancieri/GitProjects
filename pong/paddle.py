from turtle import Turtle


class Paddle(Turtle):
    """Represents a paddle in the game."""

    def __init__(self, x, y):
        """Initialize the paddle."""
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setpos(x, y)

    def move_up(self):
        """Move the paddle up."""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        """Move the paddle down."""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
