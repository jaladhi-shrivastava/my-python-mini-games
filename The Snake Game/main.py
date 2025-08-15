import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

def play_game():
    snake = Snake()
    food = Food()
    score = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")

    game = True
    while game:
        screen.update()
        time.sleep(0.1)
        snake.move()

        #detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend_body()
            score.update_score()

        #detect collision with wall
        if (snake.head.xcor() > 290 or snake.head.xcor() < -290
                or snake.head.ycor() > 290 or snake.head.ycor() < -290):
            score.game_over()
            score.display_highscore()
            game = False

        #detect collision with body
        for body in snake.snake_body[1: ]:
            if snake.head.distance(body) < 10:
                score.game_over()
                score.display_highscore()
                game = False

    # Ask if they want to play again
    rerun = screen.textinput("Play Again?", "Enter Yes or No: ")
    if rerun and rerun.lower().strip() == "yes":
        snake.reset_snake()
        score.reset_score()
        food.clear_food()
        return True


while play_game():
    pass

screen.exitonclick()