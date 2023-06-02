from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.speed("fastest")
        self.penup()
        self.goto(0, 0)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-220, 270)
        self.write(f"Level:{self.level}", align="center", font=("Courier", 16, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", font=FONT, align="center")

    def score_point(self):
        self.level += 1
        self.update_scoreboard()
