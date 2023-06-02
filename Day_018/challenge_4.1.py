from turtle import Turtle, Screen, colormode
import random

t = Turtle()
colormode(255)
t.shape("turtle")
t.pensize(5)
t.speed("fastest")

angles = [0, 90, 180, 270]


def random_path(angles):
    for _ in range(2000):
        angle = random.choice(angles)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color_tuple = (r, g, b)
        t.pencolor(color_tuple)
        t.forward(30)
        t.setheading(angle)

random_path(angles)









s = Screen()
s.exitonclick()