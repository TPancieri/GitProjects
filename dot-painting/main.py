import random
# colorgram is the package that will extract colors from an reference image
import colorgram
import turtle as t
import random as r

t.colormode(255)
rgb_colors = []

MOVE = 50

colors = colorgram.extract('image.jpg', 24)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)


def move_forward(turtle, move):
    """ Lifts the pen off and moves the pointer forward, then places the pen back down"""
    turtle.penup()
    turtle.forward(move)
    turtle.pendown()


def draw_dots(turtle, amount):
    """ Draws an amount of dots """
    for _ in range(amount):
        turtle.dot(20, random.choice(rgb_colors))
        move_forward(turtle, MOVE)


def turn_right(turtle):
    """ Turns the turtle 90 degrees to the right twice and moves it forward 50"""
    for _ in range(2):
        turtle.right(90)
        move_forward(turtle, MOVE)


def turn_left(turtle):
    """ Turns the turtle 90 degrees to the left and moves it forward 50"""
    for _ in range(2):
        turtle.left(90)
        move_forward(turtle, MOVE)


def line_draw(turtle, amount, line_pair):
    """ Draws two dotted lines"""
    for _ in range(line_pair):
        draw_dots(turtle, amount)
        turn_right(turtle)
        draw_dots(turtle, amount)
        turn_left(turtle)


timmy = t.Turtle()
timmy.speed("fastest")
timmy.hideturtle()

# Getting the pointer to the top left corner
timmy.setheading(135)  # looks to the left diagonal
move_forward(timmy, (MOVE * 8))  # moves 5 'dots' forward
timmy.setheading(0)  # sets heading back to the right

line_draw(timmy, 12, 5)

screen = t.Screen()
screen.exitonclick()
