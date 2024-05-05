import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score

# Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("blue")
screen.cv._rootwindow.resizable(False, False)
# Turn animation off, requires an screen.update()
screen.tracer(0)

# Score setup
score = Score()
# Paddle setup
left_paddle = Paddle(-350, 0)
right_paddle = Paddle(350, 0)
# Ball setup
ball = Ball()


# Listen to key press
screen.listen()
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")

# Game over condition
game_over = False
# Run the game
while not game_over:
    screen.update()
    time.sleep(ball.velocity)
    ball.move()
    # Detect top and bottom collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with the paddle, checks paddle and ball distance and x-axis position of the ball
    if ball.distance(left_paddle) < 50 and ball.xcor() > -320 or ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    # Right paddle misses
    if ball.xcor() > 380:
        ball.reset()
        score.left_scored()
    # Left paddle misses
    if ball.xcor() < -380:
        ball.reset()
        score.right_scored()




# Close screen
screen.exitonclick()
