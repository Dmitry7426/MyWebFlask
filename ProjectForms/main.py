from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, EmailField
from wtforms.validators import DataRequired, Email, Length, NumberRange, Regexp
from classuser import User

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret keys"

users = []


class MessageForms(FlaskForm):
    name = StringField("name", validators=[Length(min=5, max=30), Regexp('^[a-zA-Zа-яА-Я]+$')])
    surname = StringField("surname", validators=[Length(min=1, max=30), Regexp('^[a-zA-Zа-яА-Я]+$')])
    age = IntegerField("age", validators=[NumberRange(min=14, max=100)])
    password = StringField("password", validators=[Length(min=8, max=12), Regexp('^[a-zA-Z0-9]+$')])
    email = EmailField("email", validators=[Email()])
    submit = SubmitField("Submit")


@app.route('/')
def start():
    return render_template('index.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/newuser', methods=['GET', 'POST'])
def newUser():
    form = MessageForms()
    if form.validate_on_submit():
        name = form.name.data
        surname = form.surname.data
        age = form.age.data
        password = form.password.data
        email = form.email.data
        users.append(User(name, surname, password, email))
        # users.sort(key=User[0])


        return redirect(url_for('newUser'))

    return render_template('newuser.html', form=form)


@app.route('/users')
def us():

    return render_template('users.html', users=users)


if __name__ == '__main__':
    app.run()