# This code will not work in repl.it as there is no access to the 'colorgram' package here.###
# We talk about this in the video tutorials##

import colorgram
from turtle import Turtle, Screen, colormode
import random

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

t = Turtle()
t.speed("fastest")
t.shape("circle")
colormode(255)

y_pos = 200

for _ in range(10):

    t.penup()
    t.goto(-200, y_pos)

    for _ in range(10):
        t.color(random.choice(rgb_colors))
        t.dot(20)
        t.penup()
        t.forward(40)
        t.pendown()
        t.dot(20)

    y_pos -= 40

s = Screen()
s.exitonclick()
