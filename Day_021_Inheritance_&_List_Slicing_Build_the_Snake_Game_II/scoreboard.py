from turtle import Turtle
TEXT_ALIGN = "center"
FONT = ("Arial", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", font=FONT, align=TEXT_ALIGN)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER!", font=FONT, align=TEXT_ALIGN)
        self.goto(0, -20)
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
