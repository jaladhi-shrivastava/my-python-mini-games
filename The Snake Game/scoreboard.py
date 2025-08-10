
from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Fixedsys', 15, 'normal')
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.goto(x = 0, y = 270)
        self.write(f"SCORE: {self.score}", align=ALIGNMENT,  font=FONT)


    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"SCORE: {self.score}", align=ALIGNMENT,  font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER. \nSCORE: {self.score}", align=ALIGNMENT, font=FONT)
