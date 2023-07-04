from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1>' \
           '<p>Welcome to my flask app</p>' \
           '<img src="https://media1.giphy.com/media/tMiHhTLvQcavm/giphy.gif?cid=ecf05e47hfq3odwjz18q300ez6pv8xhgh09u5nc3yz5lv1o8&ep=v1_gifs_search&rid=giphy.gif&ct=g" width=200px>'


def make_heading(function):
    def wrapper():
        return "<h1>" + function() + "</h1>"
    return wrapper

def italize(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def underline(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route("/bye")
@make_heading
@italize
@underline
def bye():
    return "Bye!"

# To be able to pass a string to the url path as variable us the syntax <variable>
# In this code (below), the <name> specifies that anything added to the home route will be received as a variable.
# Thus for the route home/John, John is passed on as a variable and used in the function.
@app.route('/<name>')
def greet(name):
    return f'Hello, there {name}!'


# To pass an entire path as a variable, use <path:name>
@app.route('/<path:name>')
def greet_2(name):
    return f"the path: {name}"


@app.route("/<name>/<int:number>")
def greet_3(name, number):
    return f"Hello {name}, are you {number} years old?"


if __name__ == "__main__":
    app.run(debug=True)
