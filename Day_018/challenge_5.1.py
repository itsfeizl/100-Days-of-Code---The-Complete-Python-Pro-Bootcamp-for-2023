from turtle import Turtle, Screen, colormode
import random

t = Turtle()
colormode(255)
t.shape("turtle")
t.speed("fastest")


def draw_spirograph(gap_size):
    for _ in range(int(360/gap_size)):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color_tuple = (r, g, b)
        t.pencolor(color_tuple)
        t.circle(200)
        t.setheading(t.heading() + gap_size)

draw_spirograph(3)




s = Screen()
s.exitonclick()