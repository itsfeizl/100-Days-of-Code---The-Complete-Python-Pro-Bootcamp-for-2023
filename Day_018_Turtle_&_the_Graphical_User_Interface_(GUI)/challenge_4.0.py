from turtle import Turtle, Screen
import random

t = Turtle()
t.shape("turtle")
t.pensize(5)
t.speed("fastest")

colors = ["red", "green", "blue", "orange", "purple", "maroon", "aquamarine", "olive"]
angles = [0, 90, 180, 270]


def random_path(colors, angles):
    for _ in range(5000):
        angle = random.choice(angles)
        color = random.choice(colors)
        t.pencolor(color)
        t.forward(30)
        t.setheading(angle)

random_path(colors, angles)









s = Screen()
s.exitonclick()