from turtle import Turtle

# Constants
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280, 270)
        self.level = 1
        self.update_scoreboard()

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write('Level: ' + str(self.level), font=FONT)

    def game_over(self):
        self.goto(-50, 0)
        self.write('GAME OVER', font=FONT)