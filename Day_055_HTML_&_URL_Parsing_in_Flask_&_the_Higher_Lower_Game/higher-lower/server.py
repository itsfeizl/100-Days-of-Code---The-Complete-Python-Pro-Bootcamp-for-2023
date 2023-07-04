from flask import Flask
import random


app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


random_num = random.randint(0, 9)
print(random_num)


@app.route('/<int:number>')
def greet_2(number):
    f"<h1>You entered the number: {number}</h1>"
    if random_num > number:
        return f"<h1 style='color: red'>{number} is too low. Try again.</h1>" \
               f"<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif random_num < number:
        return f"<h1 style='color: red'>{number} is too high. Try again.</h1>" \
               f"<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    else:
        return f"<h1 style='color: green'>{number} is Correct. You found me.</h1>" \
               f"<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
