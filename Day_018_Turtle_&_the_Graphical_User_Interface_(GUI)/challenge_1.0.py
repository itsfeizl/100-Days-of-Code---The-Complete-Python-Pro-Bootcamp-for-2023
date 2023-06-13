from turtle import Turtle, Screen

my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("red")

def draw_square():
    my_turtle.forward(200)
    my_turtle.left(90)

for _ in range(4):
    draw_square()
































my_screen = Screen()
my_screen.exitonclick()