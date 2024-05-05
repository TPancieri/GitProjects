from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision between snake and food
    # If the snake head is within 15 pixels of the food
    if snake.head.distance(food) < 15:
        food.relocate()
        snake.grow()
        score.refresh_score()
    # Detect collision with the wall
    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 380 or snake.head.ycor() < -380:
        game_over = True
        score.game_over()
    # Detect collision with the tail
    for segment in snake.segments[2:]:
        if snake.head.distance(segment) < 10:
            game_over = True
            score.game_over()


screen.exitonclick()
