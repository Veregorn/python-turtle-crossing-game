import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from car_manager import CarManager

# Variables Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

p1 = Player()

cm = CarManager()

score = Scoreboard()

time_to_create_car = True

# Event Listener
screen.listen()
screen.onkeypress(p1.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    if time_to_create_car: # So cars only creates one of every two refreshes
        cm.create_car()
    
    time_to_create_car = not time_to_create_car
    
    cm.move_cars()
    cm.remove_outside_cars()
    
    if p1.finish_line_reached:
        score.increase_level()
        p1.change_status()
        cm.increase_cars_speed()

    # Detect collision of player with cars
    for car in cm.get_cars():
        if car.distance(p1) < 16:
            game_is_on = False

score.game_over()

# Windows closes on click
screen.exitonclick()