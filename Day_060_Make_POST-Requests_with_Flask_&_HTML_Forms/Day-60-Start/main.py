from flask import Flask, render_template, request
import requests
from datetime import datetime, date
import smtplib

OWN_EMAIL = "faisal.alhassan61@gmail.com"
OWN_PASSWORD = "jkjhrdhclxxeqsev"

datetime_now = datetime.now()
date_string = datetime_now.strftime("%d/%m/%Y")
date_today = (date(day=int(date_string[:2]), month=int(date_string[3:5]), year=int(date_string[6:])).strftime('%A %d %B %Y')).split()
today = f"{date_today[2]} {date_today[1]}, {date_today[3]}"


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


@app.route("/contact", methods=["GET", "POST"])
def contact_page():
    if request.method == "POST":
        data = request.form

        print(f"Name: {data['name']}")
        print(f"Email: {data['email']}")
        print(f"Phone: {data['phone']}")
        print(f"Message: {data['message']}")

        send_email(data["name"], data["email"], data["phone"], data["message"])

        return render_template("contact.html", msg_sent=True)

    return render_template("contact.html", msg_sent=False)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post

    return render_template("post.html", post=requested_post, today=today)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=OWN_EMAIL, password=OWN_PASSWORD)
        connection.sendmail(
            from_addr=OWN_EMAIL,
            to_addrs=OWN_EMAIL,
            msg=email_message
        )


if __name__ == "__main__":
    app.run(debug=True)