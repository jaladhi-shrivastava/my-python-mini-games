from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.speed(0)
        self.shapesize(stretch_len=0.5,stretch_wid= 0.5)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-285, 285)
        random_y = random.randint(-285, 285)
        self.goto(random_x, random_y)


