from turtle import Turtle, Screen

t = Turtle()

t.shape("turtle")
t.color("red")
t.penup()
t.goto(-100, 300)
t.pendown()

def draw_triangle():
    t.forward(200)
    t.right(120)



def draw_square():
    t.color("blue")
    t.forward(200)
    t.right(90)


def draw_pentagon():
    t.color("green")
    t.forward(200)
    t.right(72)

def draw_hexagon():
    t.color("orange")
    t.forward(200)
    t.right(60)

def draw_heptagon():
    t.color("purple")
    t.forward(200)
    t.right(51.43)

def draw_octagon():
    t.color("maroon")
    t.forward(200)
    t.right(45)

def draw_nonagon():
    t.color("indigo")
    t.forward(200)
    t.right(40)

def draw_decagon():
    t.color("olive")
    t.forward(200)
    t.right(36)



    
for _ in range(3):
    draw_triangle()

for _ in range(4):
    draw_square()

for _ in range(5):
    draw_pentagon()

for _ in range(6):
    draw_hexagon()

for _ in range(7):
    draw_heptagon()

for _ in range(8):
    draw_octagon()

for _ in range(9):
    draw_nonagon()

for _ in range(10):
    draw_decagon()














s = Screen()
s.exitonclick()