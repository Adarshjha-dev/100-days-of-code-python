import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    for car in car_manager.cars_list:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
    if player.is_at_finish_line():
        player.reset_position()
        car_manager.increase_speed()
        scoreboard.increase_level()
screen.exitonclick()
