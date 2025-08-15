

from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Fixedsys', 15, 'normal')
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.goto(x = 0, y = 270)
        self.write(f"SCORE: {self.score}|High Score: {self.highscore}", align=ALIGNMENT,  font=FONT)


    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"SCORE: {self.score}|High Score: {self.highscore}", align=ALIGNMENT,  font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0,200)
        self.write(f"GAME OVER. \nSCORE: {self.score}", align=ALIGNMENT, font=FONT)

    def display_highscore(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f'{self.highscore}')
        self.goto(0, 270)
        self.write(f"Highest Score is: {self.highscore}", align= ALIGNMENT, font=FONT)

    def reset_score(self):
        self.clear()
        self.score=0
