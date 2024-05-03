import turtle as t
import random as rand

t.colormode(255)

# Starting x point for the turtles
START_X = -375
# Max y point for a turtle to be places
MAX_Y = 250
# Finish line
FINAL_X = 375


def random_color():
    """Generate a random color tuple (R, G, B)"""
    red = rand.randint(0, 255)
    green = rand.randint(0, 255)
    blue = rand.randint(0, 255)
    return red, green, blue


def turtle_setup(turtle, current_y):
    """Set up a turtle with a random color and position"""
    r, g, b = random_color()
    turtle.shape("turtle")
    turtle.speed("fastest")
    turtle.penup()
    turtle.color(r, g, b)
    turtle.setpos(START_X, current_y)
    turtle.pendown()


def move_forward(turtle):
    """Move a turtle forward by a random distance"""
    turtle.forward(rand.randint(0, 50))


def run_race(turtle_list):
    """Run the turtle race until one reaches the finish line"""
    while all(t.xcor() <= FINAL_X for t in turtle_list):
        for runner in turtle_list:
            move_forward(runner)


def main():
    """Main entry point"""
    # Create turtles and set them up
    tim = t.Turtle()
    john = t.Turtle()
    ann = t.Turtle()
    don = t.Turtle()
    turtle_list = [tim, john, ann, don]
    separation = 0
    for runner in turtle_list:
        y_pos = MAX_Y - separation
        turtle_setup(runner, y_pos)
        separation += 150

    # Run the race
    run_race(turtle_list)

    # Set up the GUI
    screen = t.Screen()
    screen.setup(900, 700)
    screen.exitonclick()


if __name__ == "__main__":
    main()
