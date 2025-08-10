import turtle
from turtle import Turtle, Screen
import random
colors=[(161, 14, 80), (224, 144, 80), (165, 52, 100), (70, 11, 47), (155, 87, 50), (217, 214, 115), (201, 78, 113), (27, 102, 161), (17, 26, 56), (216, 91, 63), (232, 221, 189), (61, 22, 9), (203, 128, 153), (9, 32, 18), (127, 29, 19), (198, 145, 38), (209, 237, 209), (70, 111, 74), (238, 205, 217), (230, 166, 187), (46, 52, 110), (137, 141, 176), (112, 110, 177), (234, 171, 160), (129, 171, 133), (31, 83, 59), (94, 150, 101), (84, 76, 25), (9, 87, 109), (215, 221, 231), (173, 220, 148), (208, 211, 33), (39, 152, 191), (183, 184, 205)]


tutu=Turtle()
turtle.colormode(255)
tutu.penup()
tutu.hideturtle()
tutu.speed(0)
tutu.setheading(225)
tutu.forward(300)
tutu.setheading(0)

num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    choose_color = random.choice(colors)
    tutu.dot(20, choose_color)
    tutu.forward(50)

    if dot_count%10==0:
        tutu.setheading(90)
        tutu.forward(50)
        tutu.setheading(180)
        tutu.forward(500)
        tutu.setheading(0)


screen=Screen()
screen.exitonclick()