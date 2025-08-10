
from turtle import Turtle, Screen



tutu=Turtle()
screen = Screen()

def move_forward():
    tutu.forward(50)

def move_backward():
    tutu.backward(50)

def move_counter_clockwise():
    tutu.left(90)

def move_clockwise():
    tutu.right(90)

def clear_screen():
    tutu.clear()
    tutu.penup()
    tutu.home()
    tutu.pendown()

screen.listen()
screen.onkey(key= "w", fun=move_forward)
screen.onkey(key= "s", fun=move_backward)
screen.onkey(key= "a", fun=move_counter_clockwise)
screen.onkey(key= "d", fun=move_clockwise)
screen.onkey(key= "c", fun=clear_screen)






screen.exitonclick()
