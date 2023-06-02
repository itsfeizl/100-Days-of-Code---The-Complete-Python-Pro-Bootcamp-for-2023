from turtle import Turtle, Screen

t = Turtle()

t.shape("turtle")
t.color("red")

t.penup()
t.goto(-500, 0)

y_pos = -20

for _ in range(10):
    
    for _ in range(25):
        t.forward(10)
        t.penup()
        t.forward(20)
        t.pendown()
        t.forward(10)

    t.penup()
    t.goto(-500, y_pos)
    y_pos -= 20
    











s = Screen()
s.exitonclick()