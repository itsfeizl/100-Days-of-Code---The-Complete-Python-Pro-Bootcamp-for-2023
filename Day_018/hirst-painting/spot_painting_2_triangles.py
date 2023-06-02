from turtle import Turtle, Screen, colormode
import colorgram
import random

colormode(255)

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

t = Turtle()
t.speed("fastest")

y_pos = 250
x_pos = -230
num = 0

for _ in range(10):

    t.penup()
    t.goto(x_pos, y_pos)
    t.dot(20)

    for _ in range(num):
        t.color(random.choice(rgb_colors))
        t.dot(20)
        t.penup()
        t.forward(30)
        t.pendown()
        t.dot(20)
    num += 1
    y_pos -= 40


y_pos_2 = 150
x_pos_2 = 230
num = 9

for _ in range(10):

    t.penup()
    t.goto(x_pos_2, y_pos_2)
    t.dot(20)

    for _ in range(num):
        t.color(random.choice(rgb_colors))
        t.dot(20)
        t.penup()
        t.back(30)
        t.pendown()
        t.dot(20)
    num -= 1
    y_pos_2 -= 40


s = Screen()
s.exitonclick()
