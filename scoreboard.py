FONT = ("Courier", 24, "normal")


from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        
        self.level = 1
    def write_score(self):
        self.goto(-200,250)
        self.clear()
        self.write(f'Level: {self.level}', False, align="center", font=(FONT))
        
    def update_score(self):
        self.level += 1
    def game_over(self):
        self.goto(0,0)
        self.write(f'GAME OVER', False, align="center", font=(FONT))