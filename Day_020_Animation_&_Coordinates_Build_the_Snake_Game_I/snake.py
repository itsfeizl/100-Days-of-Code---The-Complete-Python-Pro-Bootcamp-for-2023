from turtle import Turtle, colormode
import random

colormode(255)

STARTING_POS = [(-20, 0), (-40, 0), (-60, 0)]
MOVE_SPEED = 20


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        # self.tail = self.snake_body[len(self.snake_body) - 1]

    # def add_body_seg(self):
    #
    #     r = random.randint(0, 255)
    #     g = random.randint(0, 255)
    #     b = random.randint(0, 255)
    #     color_tuple = (r, g, b)
    #
    #     snake_body_seg_addition = Turtle("square")
    #     snake_body_seg_addition.penup()
    #     snake_body_seg_addition.color(color_tuple)
    #     snake_body_seg_addition.goto(self.tail.xcor(), self.tail.ycor())
    #     self.snake_body.append(snake_body_seg_addition)

    def create_snake(self):
        for coordinates in STARTING_POS:
            snake_body_seg = Turtle("square")
            snake_body_seg.color("white")
            snake_body_seg.penup()
            snake_body_seg.goto(coordinates)
            self.snake_body.append(snake_body_seg)

    def move(self):
        for x in range(len(self.snake_body) - 1, 0, -1):
            new_x_cor = self.snake_body[x - 1].xcor()
            new_y_cor = self.snake_body[x - 1].ycor()
            self.snake_body[x].goto(new_x_cor, new_y_cor)

        self.head.forward(MOVE_SPEED)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
        # Alternatively:
        # if self.head.heading() == 0.0:
        #     self.snake_body[0].left(90)
        # elif self.snake_body[0].heading() == 180.0:
        #     self.snake_body[0].right(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
        # Alternatively:
        # if self.head.heading() == 0.0:
        #     self.snake_body[0].right(90)
        # elif self.snake_body[0].heading() == 180.0:
        #     self.snake_body[0].left(90)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
        # Alternatively:
        # if self.head.heading() == 90.0:
        #     self.snake_body[0].left(90)
        # elif self.snake_body[0].heading() == 270.0:
        #     self.snake_body[0].right(90)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
        # Alternatively:
        # if self.head.heading() == 90.0:
        #     self.snake_body[0].right(90)
        # elif self.snake_body[0].heading() == 270.0:
        #     self.snake_body[0].left(90)

    def snake_x_pos(self):
        return self.head.xcor()

    def snake_y_pos(self):
        return self.head.ycor()

    def jump_to(self):
        if self.head.xcor() == 300:
            self.head.goto(-300, self.head.ycor())
        elif self.head.xcor() == -300:
            self.head.goto(300, self.head.ycor())
        elif self.head.ycor() == 300:
            self.head.goto(self.head.xcor(), -300)
        elif self.head.ycor() == -300:
            self.head.goto(self.head.xcor(), 300)

    # def snake_radius(self):
    #     self.head.radius = 20
    #     return self.head.radius
