from turtle import Turtle, Screen

import random

a = Turtle()
b = Turtle()
c = Turtle()
d = Turtle()
e = Turtle()
pen = Turtle()


pen.speed("fastest")
pen.penup()
pen.goto(-240, -120)
pen.pendown()
pen.goto(-240, 120)
pen.penup()
pen.goto(240, -120)
pen.pendown()
pen.goto(240, 120)
pen.hideturtle()

a.color("red")
a.shape("turtle")
a.penup()
a.goto(-250, 100)
total_a = 0

print(a.heading())


b.color("green")
b.shape("turtle")
b.penup()
b.goto(-250, 50)
total_b = 0


c.color("blue")
c.shape("turtle")
c.penup()
c.goto(-250, 0)
total_c = 0


d.color("orange")
d.shape("turtle")
d.penup()
d.goto(-250, -50)
total_d = 0


e.color("purple")
e.shape("turtle")
e.penup()
e.goto(-250, -100)
total_e = 0


while total_a < 480 and total_b < 480 and total_c < 480 and total_d < 480 and total_e < 480:
    a_pace = random.randint(1, 5)
    a.forward(a_pace)
    total_a += a_pace

    b_pace = random.randint(1, 5)
    b.forward(b_pace)
    total_b += b_pace
#
    c_pace = random.randint(1, 5)
    c.forward(c_pace)
    total_c += c_pace

    d_pace = random.randint(1, 5)
    d.forward(d_pace)
    total_d += d_pace

    e_pace = random.randint(1, 5)
    e.forward(e_pace)
    total_e += e_pace
#
#
highest = max(total_a, total_b, total_c, total_d, total_e)

if highest == total_a:
    print("Red turtle wins!")
elif highest == total_b:
    print("Green turtle wins!")
elif highest == total_c:
    print("Blue turtle wins!")
elif highest == total_d:
    print("Orange turtle wins!")
else:
    print("Purple turtle wins!")
s = Screen()
s.exitonclick()
