from turtle import Turtle, Screen

t = Turtle()
t.penup()
t.goto(-100, 300)
t.pendown()

num_of_sides = [3, 4, 5, 6, 7, 8, 9, 10]
colors = ["red", "green", "blue", "orange", "purple", "maroon", "aquamarine", "olive"]



def draw_shapes(num_of_sides, colors):

    for num in num_of_sides: 
        angle = 360/num
        shape_color = colors[num-3]

        for _ in range(num):
            t.color(shape_color)
            t.forward(200)
            t.right(angle)

draw_shapes(num_of_sides, colors)






















s = Screen()
s.exitonclick()