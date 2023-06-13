import turtle
import pandas
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.setup(width=1000, height=1000)
screen.tracer(0)
screen.title("US States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.bgpic(image)

scoreboard = Scoreboard()

data = pandas.read_csv("50_states.csv")

states_list = data.state.to_list()
states_xcor_list = data.x.to_list()
states_ycor_list = data.y.to_list()

us_states_list = data.state.to_list()

guessed_states = []

while len(guessed_states) < 51:
    screen.update()
    answer_state = screen.textinput(title=f"{len(guessed_states)}", prompt="Name a US State").title()

    if answer_state == "Exit":
        break

    if answer_state in us_states_list:
        guessed_states.append(answer_state)
        scoreboard.score_point()

        answer_state_list = [answer_state, states_xcor_list[states_list.index(answer_state)],
                             states_ycor_list[states_list.index(answer_state)]]
        answer_state_xcor = answer_state_list[1]
        answer_state_ycor = answer_state_list[2]
        turtle.penup()
        turtle.goto(answer_state_xcor, answer_state_ycor)
        turtle.write(f"{answer_state}")
        turtle.hideturtle()

    # Alternatively:
    # if answer_state in us_states_list:
        # state_data = data[data.state == answer_state]
        # turtle.goto(int(state_data.x), int(state_data.y))
        # turtle.write(f"{answer_state}")

us_states_set = set(us_states_list)
guessed_state_set = set(guessed_states)
missed_states = list(us_states_set.difference(guessed_states))

csv_file = pandas.DataFrame(missed_states)
csv_file.to_csv("states_to_learn.csv")

print(csv_file)


# turtle.mainloop()
