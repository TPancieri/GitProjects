import turtle as t

tim = t.Turtle()
screen = t.Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def turn_counter_clock():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


# Event listeners
screen.listen()
# W -> Forward , S -> Backwards , D -> Clockwise , A -> Counter-Clockwise
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="d", fun=turn_clockwise)
screen.onkeypress(key="a", fun=turn_counter_clock)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
