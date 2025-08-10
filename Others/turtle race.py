import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "blue", "green", "purple"]
turtles = []
tutu=Turtle()
tutu.hideturtle()
tutu.penup()
tutu.goto(0,150)

def start_position():
    turtles.clear()
    screen.clear()
    screen.setup(width=500, height=400)
    start_y = -100
    for t_index in range(6):
        t = Turtle(shape="turtle")
        t.hideturtle()
        t.speed(0)
        t.penup()
        t.color(colors[t_index])
        t.goto(-200, start_y)
        t.showturtle()
        start_y += 40
        turtles.append(t)

game = True
races=0
won=0
lost=0
while game:
    start_position()

    # Keep asking until valid color is entered
    while True:
        user_bet = screen.textinput(
            title="Make a bet!",
            prompt=f"Which turtle will win the race? Choose from {', '.join(colors)}: "
        )
        if not user_bet:  # user closed dialog
            game = False
            break
        user_bet = user_bet.lower().strip()
        if user_bet in colors:
            races+=1
            tutu.clear()
            break
        tutu.clear()
        tutu.write("Invalid color. Please try again.", align="center", font=("Arial", 16, "normal"))


    if not game:
        break

    # Run the race
    is_on = True
    while is_on:
        for run in turtles:
            run.forward(random.randint(0, 10))
            if run.xcor() > 230:
                winner_color = run.pencolor()
                if winner_color == user_bet:
                    won+=1
                    tutu.clear()
                    tutu.write(f"Hurray! You won. \nThe winner is {winner_color} turtle.",
                               align="center", font=("Arial", 16, "normal"))
                else:
                    lost+=1
                    tutu.clear()
                    tutu.write(f"Oopsie! You lost. \nThe winner is {winner_color} turtle.",
                               align="center", font=("Arial", 16, "normal"))
                is_on = False
                break

    # Ask if they want to play again
    rerun = screen.textinput(
        title="Do you want to bet again?",
        prompt="Enter Yes or No: "
    )
    if not rerun or rerun.lower().strip() != "yes":
        game = False

tutu.goto(0,0)
tutu.clear()
tutu.write(f"Thanks for playing. You played {races} races. \n"
           f"Won- {won} \n"
           f"Lost- {lost} \n"
           f"Click anywhere on the screen to exit.\n",
           align="center", font=("Arial", 16, "normal"))


screen.exitonclick()
