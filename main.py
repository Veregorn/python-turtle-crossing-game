import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Variables Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

p1 = Player()

# Event Listener
screen.listen()
screen.onkeypress(p1.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
