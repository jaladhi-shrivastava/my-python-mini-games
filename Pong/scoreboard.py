# scoreboard.py
from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Fixedsys', 60, 'normal')
R_SCORE_POS = (100, 200)
L_SCORE_POS = (-100, 200)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.right_score = 0
        self.left_score = 0
        self.divider_segments = []

        self.draw_divider(True)
        self.update_score()

    def draw_divider(self, game=True):
        if game:

            if self.divider_segments:
                return
            for y in range(280, -280, -40):
                seg = Turtle(visible=False)
                seg.color("white")
                seg.shape("square")
                seg.penup()
                seg.shapesize(stretch_wid=1, stretch_len=0.5)
                seg.goto(0, y)
                seg.showturtle()
                self.divider_segments.append(seg)
        else:
            # remove all segments
            for seg in self.divider_segments:
                seg.clear()
                seg.hideturtle()
            self.divider_segments.clear()

    def update_score(self):
        self.clear()
        self.goto(L_SCORE_POS)
        self.write(self.left_score, align=ALIGNMENT, font=FONT)
        self.goto(R_SCORE_POS)
        self.write(self.right_score, align=ALIGNMENT, font=FONT)

    def right_point(self):
        self.right_score += 1
        self.update_score()

    def left_point(self):
        self.left_score += 1
        self.update_score()

    def game_over(self):
        self.clear()
        self.draw_divider(False)  # hide divider segments
        winner = "Right" if self.right_score > self.left_score else "Left"
        self.goto(0, 0)
        self.write(f"GAME OVER!\nThe winner is {winner}\nRight Score- {self.right_score}\nLeft Score- {self.left_score}",
                   align=ALIGNMENT, font=("Arial", 16, "normal"))
        self.getscreen().update()
