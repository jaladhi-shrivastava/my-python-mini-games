from turtle import Screen
from paddle import Paddle
from striker import Striker
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("The Pong Game")
screen.tracer(0)

# Ask for game mode
game_mode = screen.numinput(
    title="Game Mode",
    prompt="Enter '1' for Single Player or '2' for Two Player:"
)
if game_mode not in [1, 2]:
    print("Invalid choice. Defaulting to 1 Player vs AI.")
    game_mode = 1

# Create paddles, ball, and scoreboard
right_paddle = Paddle(x_pos=370, y_pos=0)
left_paddle = Paddle(x_pos=-370, y_pos=0)
ball = Striker()
score = Scoreboard()

# Ask for score limit
score_limit = screen.numinput(
    title="Score Limit",
    prompt="Enter score limit. [5/9/11]: ",
    default=11,
    minval=5,
    maxval=15
)

# Key bindings
screen.listen()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")

if game_mode == 2:
    screen.onkeypress(left_paddle.up, "w")
    screen.onkeypress(left_paddle.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # AI control only in single-player mode
    if game_mode == 1 and ball.move_x < 0:
        left_paddle.follow_ball(ball)  # We'll add this method in Paddle class

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Right paddle misses
    if ball.xcor() > 380:
        ball.refresh_position()
        score.left_point()

    # Left paddle misses
    if ball.xcor() < -380:
        ball.refresh_position()
        score.right_point()

    # Right paddle hits
    if ball.distance(right_paddle) < 50 and ball.xcor() > 340:
        ball.bounce_x(right_paddle)

    # Left paddle hits
    if ball.distance(left_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x(left_paddle)

    # Track the score and check for game over
    if score.right_score == score_limit or score.left_score == score_limit:
        score.game_over()
        ball.clear_ball()
        break

screen.exitonclick()
