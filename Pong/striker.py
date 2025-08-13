
from turtle import Turtle

class Striker(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0,0)
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_x = 10
        self.move_y = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)


    def bounce_y(self):
        self.move_y *= -1
        self.move_speed *= 0.9

    def bounce_x(self, paddle):
        offset = self.ycor() - paddle.ycor()
        angle_factor = offset / 50
        angle_factor = max(-0.9, min(0.9, angle_factor))
        self.move_y = angle_factor * abs(self.move_x)
        self.move_x *= -1
        self.move_speed *= 0.9

    def refresh_position(self):
        self.goto(0,0)
        self.move_speed = 0.1

    def clear_ball(self):
        self.hideturtle()
        self.getscreen().update()