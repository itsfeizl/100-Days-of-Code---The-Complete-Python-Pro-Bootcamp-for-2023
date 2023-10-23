# import modules
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from bs4 import BeautifulSoup
import requests

CHATGPT_API_NAME = "Myname=Faisal+Alhassan"
CHATGPT_API_KEY = "Bearer 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"
chatgpt_ai_endpoint = "https://api.openai.com/v1/chat/completions"


# create the app
app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
# database name is library-movies-collection
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///briefer_copy_posts.db"

# create the extension
db = SQLAlchemy()

# initialize the database
db.init_app(app)


# create table model. table is named book with columns: id, title, author, and rating
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    headline = db.Column(db.String(250), nullable=False)
    content = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    source = db.Column(db.String, nullable=False)
    source_url = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f'<Movie {self.title}>'


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    result = db.session.execute(db.select(Post).order_by(desc(Post.date)))
    all_posts = result.scalars()

    post_list = []

    for post in all_posts:
        # Access the attributes or properties of the 'Post' object
        post_data = {
            'id': post.id,
            'headline': post.headline,
            'content': post.content,
            'category': post.category,
            'source': post.source,
            'source-url': post.source_url,
            'date': post.date
            # Add more attributes as needed
        }

        post_list.append(post_data)

    politics_posts = [item for item in post_list if item["category"] == "Politics"]
    business_posts = [item for item in post_list if item["category"] == "Business"]
    entertainment_posts = [item for item in post_list if item["category"] == "Showbiz"]
    sports_posts = [item for item in post_list if item["category"] == "Sports"]

    return render_template("index.html", politics_posts=politics_posts, business_posts=business_posts,
                           sports_posts=sports_posts, entertainment_posts=entertainment_posts)


@app.route("/add-post", methods=["GET", "POST"])
def add_post():
    if request.method == "POST":
        news_link = request.form["source-url"]
        category = request.form["category"]
        source = request.form["source"]
        date = "12th June, 2023"

        response = requests.get(news_link)
        soup = BeautifulSoup(response.text, "html.parser")

        article = soup.select_one(selector=".article-details")
        title = article.select_one(selector="h1").getText()
        raw_content = ""
        paragraph_list = article.select(selector="p")
        for p in paragraph_list[:-2]:
            raw_content += p.getText()

        params = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": f"Summarize this text in 50 words: {raw_content}"}]
        }

        headers = {
            "Authorization": CHATGPT_API_KEY
        }

        response = requests.post(url=chatgpt_ai_endpoint, stream=True, json=params, headers=headers)
        content_summary = response.json()["choices"][0]["message"]["content"]

        # CREATE RECORD
        new_post = Post(
            headline=title,
            content=content_summary,
            category=category,
            source=source,
            source_url=news_link,
            date=date
        )
        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template("add-post.html")


@app.route('/dashboard')
def dashboard():
    result = db.session.execute(db.select(Post))
    all_posts = result.scalars()
    return render_template("dashboard.html", posts=all_posts)


@app.route("/edit-post", methods=["GET", "POST"])
def edit_post():

    if request.method == "POST":
        # UPDATE RECORD
        post_id = request.form["id"]
        post_to_update = db.get_or_404(Post, post_id)
        post_to_update.title = request.form["headline"]
        post_to_update.author = request.form["content"]
        post_to_update.rating = request.form["category"]
        post_to_update.rating = request.form["source"]
        post_to_update.rating = request.form["source-url"]
        post_to_update.rating = request.form["date"]
        db.session.commit()

        return redirect(url_for('home'))

    post_id = request.args.get('id')
    post_selected = db.get_or_404(Post, post_id)

    return render_template("edit-post.html", post=post_selected)


@app.route("/delete-post")
def delete_post():
    post_id = request.args.get('id')

    # DELETE A RECORD BY ID
    post_to_delete = db.get_or_404(Post, post_id)
    # Alternative way to select the book to delete.
    # book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
