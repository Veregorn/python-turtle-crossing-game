from turtle import Turtle
import random

# Constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Car(Turtle):
    def __init__(self, move_distance) -> None:
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(COLORS[random.randint(0, len(COLORS) - 1)])
        self.penup()
        self.goto(320, random.randint(-300, 300))
        self.current_move_distance = move_distance

    def move(self):
        self.goto(self.xcor() - self.current_move_distance, self.ycor())

    def delete(self):
        self.delete()

    def increase_move_distance(self):
        self.current_move_distance += MOVE_INCREMENT

class CarManager():
    
    def __init__(self) -> None:
        self.cars = []
        self.current_move_distance = STARTING_MOVE_DISTANCE
        
    def create_car(self):
        car = Car(self.current_move_distance)
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.move()

    def remove_outside_cars(self):
        new_cars = []

        for car in self.cars:
            if car.xcor() > -320:
                new_cars.append(car)
            else:
                car.hideturtle()

        self.cars = new_cars

    def increase_cars_speed(self):
        self.current_move_distance += MOVE_INCREMENT
        for car in self.cars:
            car.increase_move_distance()