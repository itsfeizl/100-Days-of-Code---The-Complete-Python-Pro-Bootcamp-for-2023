from turtle import Turtle, Screen

t = Turtle()
t.shape("turtle")
t.color("red")

t.penup()
t.goto(-100, 300)
t.pendown()

colors = ["red", "green", "blue", "orange", "purple", "maroon", "aquamarine", "olive"]

def draw_shapes(sides): 
    angle = 360/sides
    color = colors[sides - 3]

    for _ in range(sides):
        t.color(color)
        t.forward(200)
        t.right(angle)


for num_of_sides in range(3, 11):
    draw_shapes(num_of_sides)











s = Screen()
s.exitonclick()