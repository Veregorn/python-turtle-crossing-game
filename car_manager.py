from turtle import Turtle
import random

# Constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Car(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(COLORS[random.randint(0, len(COLORS) - 1)])
        self.penup()
        self.goto(320, random.randint(-300, 300))

    def move(self):
        self.goto(self.xcor() - STARTING_MOVE_DISTANCE, self.ycor())

    def delete(self):
        self.delete()

class CarManager():
    
    def __init__(self) -> None:
        self.cars = []
        
    def create_car(self):
        car = Car()
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