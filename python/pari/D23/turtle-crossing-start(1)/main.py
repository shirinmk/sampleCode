import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
# listen for key up screen
screen.listen()
screen.onkey(player.moveUp, "Up")

# create car
car = CarManager()

# create several car moving right to left

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car.create_car()
    car.move()
    screen.update()

