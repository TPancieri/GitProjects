import time
from turtle import Screen
from level_control import Level
from player import Player
from car_spawner import Car

# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("blue")
screen.title("Turtle crossing")
# Lock screen resizing
screen.cv._rootwindow.resizable(False, False)
# Disable tracers !! requires screen.update() !!
screen.tracer(0)

#  Level counter setup
level = Level()
# Turtle player setup
player = Player()
# Car setup
cars = Car()


# Setup key listeners
screen.listen()
screen.onkeypress(player.move, "Up")

game_over = False
while not game_over:
    # While the player has not reached level 6
    time.sleep(0.1)
    screen.update()
    # Create a car every 0.1
    cars.create_car()
    # Move cars to the left bound
    cars.move_car()

    # Detect collision with the car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            level.game_over_screen()
            game_over = True
    # While player has not reached the last level
    if level.level < 5:
        # Check the player position relative to the finish line
        if player.ycor() >= 280:
            # When player reaches finish line increase level and restart player position
            level.increase_level()
            player.start_point()
            cars.level_up()
    # If player has reached the last level
    if level.level >= 5:
        # End the game with a winning screen
        level.winner_screen()
        game_over = True



# Close on click
screen.exitonclick()
