import turtle as t
import random


def random_color():
    """Returns a random RGB color tuple"""
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b


class TurtleMover:
    FULL_CIRCLE = 360

    def __init__(self, turtle):
        self.turtle = turtle

    def draw_shape(self, sides, size):
        """Draws a shape with the given number of sides and size"""
        angle = self.FULL_CIRCLE / sides
        for _ in range(sides):
            r, g, b = random_color()
            self.turtle.color(r, g, b)
            self.turtle.forward(size)
            self.turtle.left(angle)

    def dashed_line(self, size, dashes):
        """Draws a dashed line with the given size and number of dashes"""
        for _ in range(dashes):
            self.turtle.forward(size)
            self.turtle.penup()
            self.turtle.forward(size)
            self.turtle.pendown()

    def random_walk(self, size, paces):
        """Performs a random walk with the given step size and number of paces"""
        directions = [0, 90, 180, 270]
        for _ in range(paces + 1):
            r, g, b = random_color()
            self.turtle.color(r, g, b)
            self.turtle.forward(size)
            self.turtle.setheading(random.choice(directions))

    def draw_circle(self, radius, extent, steps):
        """Draws a circle with the given radius, extent, and number of steps"""
        self.turtle.circle(radius, extent, steps)

    def spirograph(self, radius, extent, steps, divisions):
        """Draws a spirograph with the given radius, extent, steps, and divisions"""
        # can't have divide by 0
        if not isinstance(divisions, int) or divisions <= 0:
            raise ValueError("Divisions must be a positive integer")
        # get the degree amount that the turtle will spin
        angle_turn = self.FULL_CIRCLE / divisions
        # define the starting point
        start_heading = self.turtle.heading()
        # define a second point for comparison
        current_heading = start_heading + angle_turn
        # while the second point doesn't reach the starting point, i.e. while it does a full circle
        while start_heading != current_heading < self.FULL_CIRCLE:
            # Pick a random color
            r, g, b = random_color()
            self.turtle.color(r, g, b)
            # Draw the circle
            self.draw_circle(radius, extent, steps)
            # Rotate the pointer by the spin angle
            self.turtle.left(angle_turn)
            current_heading = self.turtle.heading()


if __name__ == "__main__":
    timmy = t.Turtle()
    timmy.pensize(5)
    timmy.speed("fastest")
    mover = TurtleMover(timmy)
    mover.spirograph(100, None, None, 50)

    screen = t.Screen()
    screen.exitonclick()
