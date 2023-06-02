from turtle import Turtle, Screen, colormode
import random

t = Turtle()
colormode(255)
t.shape("turtle")
t.speed("fastest")



tilt_amnt = -3

for x in range (120):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    t.pencolor(color_tuple)
    t.circle(200)
    t.right(tilt_amnt)
    













s = Screen()
s.exitonclick()