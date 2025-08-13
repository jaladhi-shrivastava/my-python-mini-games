
from turtle import Turtle
MOVE_DISTANCE = 20

class Paddle(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid= 5, stretch_len=1)
        self.goto(x=x_pos, y=y_pos)


    def up(self):
        if not self.ycor() > 280:
            new_y = self.ycor()  + 20
            self.goto(x=self.xcor(),y= new_y )


    def down(self):
        if not self.ycor() < -280:
            new_y = self.ycor() - 20
            self.goto(x=self.xcor(), y=new_y)

    def follow_ball(self, ball):
        # Only move if the ball is coming towards the left side
        if ball.move_x < 0:
            # Get vertical distance to the ball
            distance_y = ball.ycor() - self.ycor()

            # Add a small reaction threshold (dead zone)
            if abs(distance_y) > 10:
                # Limit movement speed so AI is beatable
                move_amount = min(12, max(-12, distance_y))
                self.goto(self.xcor(), self.ycor() + move_amount)
