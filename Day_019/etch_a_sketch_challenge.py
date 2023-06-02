from turtle import Turtle, Screen

# import random

t = Turtle()


def move_forwards():
    t.forward(10)


def move_backwards():
    t.backward(10)


def turn_left():
    t.left(10)


def turn_right():
    t.right(10)


def delete_move():
    t.undo()


def clear_screen():
    t.clear()
    t.penup()
    t.home()


s = Screen()
s.listen()
s.onkey(move_forwards, "w")
s.onkey(move_backwards, "s")
s.onkey(turn_left, "a")
s.onkey(turn_right, "d")
s.onkey(clear_screen, "Delete")
s.onkey(delete_move, "Left")
s.exitonclick()
