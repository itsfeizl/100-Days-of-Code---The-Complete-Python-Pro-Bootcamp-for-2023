from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
import email_validator
from flask_bootstrap import Bootstrap5


class LoginForm(FlaskForm):
    name = StringField(label="Name", validators=[DataRequired()])
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=8, max=30)])
    submit = SubmitField(label="Log in")


app = Flask(__name__)
bootstrap = Bootstrap5(app)

app.secret_key = "This_here_is_my_secret"


@app.route("/")
def home():
    return render_template('index.html', bootstrap=bootstrap)


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        print(login_form.name.data)
        print(login_form.email.data)
        print(login_form.password.data)
        if login_form.name.data == "Faisal Alhassan" and login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html", bootstrap=bootstrap)
        else:
            return render_template("denied.html", bootstrap=bootstrap)
    return render_template('login_bootstrap.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
