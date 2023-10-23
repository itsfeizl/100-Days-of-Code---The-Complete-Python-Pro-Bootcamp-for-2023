# import modules
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge
from werkzeug.datastructures import FileStorage

import os

# create the app
app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
# database name is library-movies-collection
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my-top-ten-movies.db"

# create the extension
db = SQLAlchemy()

# initialize the database
db.init_app(app)


# create table model. table is named book with columns: id, title, author, and rating
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    img_url = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    running_time = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    director = db.Column(db.String(250), nullable=False)
    cast = db.Column(db.String(250), nullable=False)
    about = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Movie {self.title}>'


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    result = db.session.execute(db.select(Movie).order_by(desc(Movie.rating)))
    all_movies = result.scalars()
    return render_template("index.html", movies=all_movies)


@app.route('/home_page')
def home_page():
    result = db.session.execute(db.select(Movie).order_by(desc(Movie.rating)))
    all_movies = result.scalars()


    return render_template("home_page.html", movies=all_movies)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # CREATE RECORD
        new_movie = Movie(
            title=request.form["title"],
            img_url=request.form["img_url"],
            year=request.form["year"],
            running_time=request.form["running-time"],
            genre=request.form["genre"],
            rating=request.form["rating"],
            director=request.form["director"],
            cast=request.form["cast"],
            about=request.form["about"]
        )
        db.session.add(new_movie)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template("add.html")


@app.route("/edit_movie", methods=["GET", "POST"])
def edit_movie():

    if request.method == "POST":
        # UPDATE RECORD
        movie_id = request.form["id"]
        movie_to_update = db.get_or_404(Movie, movie_id)
        movie_to_update.title = request.form["title"]
        movie_to_update.img_url = request.form["img_url"]
        movie_to_update.year = request.form["year"]
        movie_to_update.running_time = request.form["running-time"]
        movie_to_update.genre = request.form["genre"]
        movie_to_update.director = request.form["director"]
        movie_to_update.rating = request.form["rating"]
        movie_to_update.cast = request.form["cast"]
        movie_to_update.about = request.form["about"]

        db.session.commit()

        return redirect(url_for('home'))

    movie_id = request.args.get('id')
    movie_selected = db.get_or_404(Movie, movie_id)

    return render_template("edit_movie.html", movie=movie_selected)


@app.route("/delete")
def delete():
    movie_id = request.args.get('id')

    # DELETE A RECORD BY ID
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/serve-image/<filename>", methods=["GET"])
def serve_image(filename):
    return send_from_directory(app.config["UPLOADS_DIRECTORY"], filename)


if __name__ == "__main__":
    app.run(debug=True)

