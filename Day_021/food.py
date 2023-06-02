from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh()

    def refresh(self):
        random_x_pos = random.randint(-280, 280)
        random_y_pos = random.randint(-280, 280)
        self.goto(random_x_pos, random_y_pos)

    def add_score(self):
        pass
