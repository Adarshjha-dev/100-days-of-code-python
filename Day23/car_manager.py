from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "cyan", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        self.cars_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.pu()
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.cars_list.append(new_car)

    def move(self):
        for car in self.cars_list:
            car.backward(self.car_speed)
        self.cars_list = [car for car in self.cars_list if car.xcor() > -320]

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
