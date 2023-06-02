from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 120)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        self.goto(0, 100)
        self.write(f"Your score is {self.score}", align=ALIGNMENT, font=("Courier", 18, "normal"))
        if self.score > self.high_score:
            self.goto(0, 80)
            self.write(f"You've set a new high score.", align=ALIGNMENT, font=("Courier", 18, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
