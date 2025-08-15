from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_square(position)


    def add_square(self, position):
        square = Turtle("square")
        square.color("white")
        square.penup()
        square.goto(position)
        self.snake_body.append(square)

    def extend_body(self):
        self.add_square(self.snake_body[-1].position())


    def move(self):
        for squares in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[squares - 1].xcor()
            new_y = self.snake_body[squares - 1].ycor()
            self.snake_body[squares].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def reset_snake(self):
        for squares in self.snake_body:
            squares.hideturtle()
        self.snake_body.clear()

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)