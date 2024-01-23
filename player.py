from turtle import Turtle

# Constants
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 300

class Player(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)
        self.finish_line_reached = False

    def change_status(self):
        self.finish_line_reached = not self.finish_line_reached

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def move(self):
        self.goto(0, self.ycor() + MOVE_DISTANCE)

        if self.ycor() > FINISH_LINE_Y:
            self.change_status()
            self.reset_position()
