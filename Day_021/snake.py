from turtle import Turtle

STARTING_POS = [(-20, 0), (-40, 0), (-60, 0)]
MOVE_SPEED = 20


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for coordinates in STARTING_POS:
            self.add_snake_body_seg(coordinates)

    def add_snake_body_seg(self, coordinates):
        snake_body_seg = Turtle("square")
        snake_body_seg.color("white")
        snake_body_seg.penup()
        snake_body_seg.goto(coordinates)
        self.snake_body.append(snake_body_seg)

    def grow_snake(self):
        self.add_snake_body_seg(self.snake_body[-1].position())

    def move(self):
        for x in range(len(self.snake_body) - 1, 0, -1):
            new_x_cor = self.snake_body[x - 1].xcor()
            new_y_cor = self.snake_body[x - 1].ycor()
            self.snake_body[x].goto(new_x_cor, new_y_cor)

        self.head.forward(MOVE_SPEED)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
