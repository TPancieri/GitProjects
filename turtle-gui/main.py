import turtle as t
import random

timmy = t.Turtle()

# timmy.shape("circle")
# timmy.color("blue")
directions = [0,90,180,270]


def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b


def draw_shape(turtle, sides, size):
    angle = 360/sides
    for _ in range(sides):
        r, g, b = random_color()
        turtle.color(r, g, b)
        turtle.forward(size)
        turtle.left(angle)


# for i in range(3, 11):
    # draw_shape(timmy, i, 100)


def dashed_line(turtle, size, dashes):
    for _ in range(dashes):
        turtle.forward(size)
        turtle.penup()
        turtle.forward(size)
        turtle.pendown()


def random_walk(turtle,size, paces):
    for _ in range(paces+1):
        r,g,b = random_color()
        turtle.color(r,g,b)
        turtle.forward(size)
        turtle.setheading(random.choice(directions))

timmy.pensize(25)
timmy.speed("fastest")
random_walk(timmy,100,50)


screen = t.Screen()
screen.exitonclick()
