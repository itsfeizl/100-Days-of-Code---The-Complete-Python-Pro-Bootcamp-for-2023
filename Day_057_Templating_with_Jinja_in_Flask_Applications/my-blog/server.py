from flask import Flask, render_template
from datetime import datetime
import requests


app = Flask(__name__)
date = datetime.now().year

@app.route('/')
def home():
    return render_template("index.html", date=date)


@app.route('/guess/<name>')
def guess(name):
    param = {
        "name": name,
    }
    gender_response = requests.get("https://api.genderize.io?", params=param)
    gender = gender_response.json()["gender"]

    age_response = requests.get("https://api.agify.io?", params=param)
    age = age_response.json()["age"]

    return render_template("index.html", name=name, gender=gender, age=age)


@app.route('/blog')
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts, date=date)


if __name__ == "__main__":
    app.run(debug=True)