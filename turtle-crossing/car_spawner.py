from turtle import Turtle, colormode
import random

colormode(255)
START_MOVE_SPEED = 5
SPEED_INCREMENT = 10


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 120)
    return red, green, blue


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.all_cars = []
        self.car_speed = START_MOVE_SPEED

    def create_car(self):
        random_chance = random.randint(1,6)
        # only create a car 1 in 6 times
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            r, g, b = random_color()
            new_car.color(r, g, b)
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += SPEED_INCREMENT
