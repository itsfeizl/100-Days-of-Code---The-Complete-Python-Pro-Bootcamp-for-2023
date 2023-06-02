import turtle
from turtle import Screen, write
from snake import Snake
import time

s = Screen()
s.title("Snake Game")
s.setup(width=600, height=600)
s.bgcolor("black")
s.tracer(0)

snake = Snake()

s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.right, "Right")
s.onkey(snake.left, "Left")

game_on = True
while game_on:

    s.update()
    time.sleep(0.1)

    snake.move()

    if snake.snake_x_pos() == 300 or snake.snake_x_pos() < -300 or snake.snake_y_pos() > 300 or snake.snake_y_pos() == -300:
        turtle.color("white")
        write("Game Over", font=("Arial", 21, "normal"), align="center")
        game_on = False

s.exitonclick()
