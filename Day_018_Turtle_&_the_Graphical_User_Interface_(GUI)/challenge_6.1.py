from turtle import Turtle, Screen, colormode
import random

colormode(255)
t = Turtle()
t.penup()

t.left(90)

angle = 10
move = 40
x_pos = -230
range_num = 36

 


t.goto(x_pos, 0)

for x in range(36):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    t.color(color)

    t.dot(20)
    t.penup()
    t.forward(move)
    t.right(angle)



t.goto(x_pos + 40, 0)

for x in range(30):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    t.color(color)
            
    t.dot(20)
    t.penup()
    t.forward(move)
    t.right(angle + 2)


t.goto(x_pos + 80, 0)

for x in range(24):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    t.color(color)
            
    t.dot(20)
    t.penup()
    t.forward(move)
    t.right(angle + 5)


t.goto(x_pos + 120, 0)

for x in range(18):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    t.color(color)
            
    t.dot(20)
    t.penup()
    t.forward(move)
    t.right(angle + 10)


t.goto(x_pos + 160, 0)

for x in range(12):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    t.color(color)
            
    t.dot(20)
    t.penup()
    t.forward(move)
    t.right(angle + 20)


t.goto(x_pos + 200, 0)

for x in range(6):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    t.color(color)
            
    t.dot(20)
    t.penup()
    t.forward(move)
    t.right(angle + 50)


t.goto(x_pos + 235, 20)

for x in range(1):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    t.color(color)
            
    t.dot(20)
    t.penup()
    t.forward(move)
    t.right(angle + 50)
    t.pendown()
    
    





s = Screen()
s.exitonclick()