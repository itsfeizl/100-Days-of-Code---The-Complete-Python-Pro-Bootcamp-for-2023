from turtle import Turtle, Screen
import random

s = Screen()
s.setup(width=500, height=400)

player_choice = s.textinput(title="Place bet:", prompt="Which turtle do you pick to win? ")

colors = ["red", "yellow", "green", "blue", "orange", "purple"]
turtles_list = []
y_pos = 80

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-240, y_pos)
    turtles_list.append(new_turtle)

    y_pos -= 30

race_on = False

if player_choice:
    race_on = True

while race_on:

    for turtle in turtles_list:

        if turtle.xcor() > 220:
            race_on = False
            winner_color = turtle.pencolor()
            if winner_color == player_choice:
                print(f"You win. The {winner_color} turtle is the winner.")
            else:
                print(f"You've lost. The {winner_color} turtle is the winner.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


s.exitonclick()
