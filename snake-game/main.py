import turtle
import random

# Starting the "snake" up
sam = turtle.Turtle()
sam.shape("square")
sam.speed("slow")
sam.color("white")
sam.penup()
sam_len = 4

# Declaring game state
game_over = False
score = 0
fruit_present = False

# Set up the screen
screen = turtle.Screen()
screen.screensize(canvwidth=900, canvheight=800, bg="black")
# Block resizing the window
screen.cv._rootwindow.resizable(False, False)

# Defining screen bound
wn = turtle.Screen()
LEFT_BOUND = -wn.window_width() / 2
RIGHT_BOUND = wn.window_width() / 2
TOP_BOUND = wn.window_height() / 2
BOTTOM_BOUND = -wn.window_height() / 2

# Writing score on top of screen
score_txt = turtle.Turtle()
score_txt.color("white")
score_txt.penup()
score_txt.hideturtle()
# Placing the txt a little below the top_bound
txt_y = TOP_BOUND - 50
score_txt.setpos(0, txt_y)
# Write score
score_txt.write(arg=f"Score : {score}", move=False, align="center", font=("Verdana", 15, "normal"))


def move():
    sam.forward(10)


def turn_north():
    sam.setheading(90)


def turn_east():
    sam.setheading(0)


def turn_west():
    sam.setheading(180)


def turn_south():
    sam.setheading(270)


def check_border():
    sam.speed("fastest")
    if sam.xcor() > RIGHT_BOUND:
        sam.goto(LEFT_BOUND, sam.ycor())
    if sam.xcor() < LEFT_BOUND:
        sam.goto(RIGHT_BOUND, sam.ycor())
    if sam.ycor() > TOP_BOUND:
        sam.goto(sam.xcor(), BOTTOM_BOUND)
    if sam.ycor() < BOTTOM_BOUND:
        sam.goto(sam.xcor(), TOP_BOUND)
    sam.speed("fast")


def spawn_fruit(turt):
    fruit_x = random.uniform(LEFT_BOUND, RIGHT_BOUND)
    fruit_y = random.uniform(BOTTOM_BOUND, TOP_BOUND)
    turt.setpos(fruit_x, fruit_y)
    present = True
    return present


def check_collision(food, snake, ):
    if abs(food.xcor() - snake.xcor()) < 8 and abs(food.ycor() - snake.ycor()) < 8:
        collision = True
        food.clear()
        return collision


def increase_size(len):
    sam.shapesize(stretch_len=len)


# Set up fruit
fruit = turtle.Turtle()
fruit.shape("circle")
fruit.color("blue")
fruit.penup()

screen.listen()
while not game_over:
    # Move turtle
    move()
    # Check for border collision
    check_border()
    # Spawn a fruit if none are in screen
    if not fruit_present:
        fruit_present = spawn_fruit(fruit)
    # Check if snake passed above fruit
    collided = check_collision(fruit, sam)
    if collided:
        score_txt.clear()
        score_txt.write(arg=f"Score : {score}", move=False, align="center", font=("Verdana", 15, "normal"))
        score += 1
        increase_size(sam_len)
        sam_len += 2
    screen.onkey(key="w", fun=turn_north)
    screen.onkey(key="a", fun=turn_west)
    screen.onkey(key="s", fun=turn_south)
    screen.onkey(key="d", fun=turn_east)

screen.exitonclick()

# TODO make an end/death state if the snake head touches the body
