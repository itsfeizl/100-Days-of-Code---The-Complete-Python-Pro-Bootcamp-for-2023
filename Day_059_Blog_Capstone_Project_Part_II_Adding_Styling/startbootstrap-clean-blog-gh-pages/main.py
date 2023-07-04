from flask import Flask, render_template
import requests
from datetime import datetime, date


datetime_now = datetime.now()
print(datetime_now)
date_string = datetime_now.strftime("%d/%m/%Y")
print(date_string)

date_today = (date(day=int(date_string[:2]), month=int(date_string[3:5]), year=int(date_string[6:])).strftime('%A %d %B %Y')).split()
print(date_today)
today = f"{date_today[2]} {date_today[1]}, {date_today[3]}"
print(today)


blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
posts = requests.get(blog_url).json()


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template("index.html", posts=posts, today=today)


@app.route('/about')
def about_page():
    return render_template("about.html")


@app.route('/contact')
def contact_page():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post

    return render_template("post.html", post=requested_post, today=today)


if __name__ == "__main__":
    app.run(debug=True)