from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def receive_data():
    f_name = request.form["fname"]
    l_name = request.form["lname"]
    password = request.form["password"]

    return f"<h1>First name: {f_name}</h1>" \
           f"<h1>Last name: {l_name}</h1>" \
           f"<h1>Password: {password}</h1>"


if __name__ == "__main__":
    app.run(debug=True)