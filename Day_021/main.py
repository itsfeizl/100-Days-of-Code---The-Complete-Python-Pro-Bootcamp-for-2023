from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_on = True
while game_on:

    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow_snake()
        scoreboard.increase_score()

    # Detect collision with tail
    for snake_body_seg in snake.snake_body[1:]:
        if snake.head.distance(snake_body_seg) < 10:
            game_on = False
            scoreboard.game_over()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        scoreboard.game_over()


screen.exitonclick()
