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

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="w", fun=snake.up)
screen.onkey(key="a", fun=snake.left)
screen.onkey(key="s", fun=snake.down)
screen.onkey(key="d", fun=snake.right)

game_is_on = True
scoreboard.update_scoreboard()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.calculate_score()
        snake.extend()
        food.refresh()

    # Detect collision with wall
    if (snake.head.xcor() > 290) or (snake.head.xcor() < -290) or (snake.head.ycor() > 290) or (snake.head.ycor() < -290):
        scoreboard.reset_game()
        snake.reset_snake()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_game()
            snake.reset_snake()

screen.exitonclick()
