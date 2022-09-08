from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, EmailField
from wtforms.validators import DataRequired, Email, Length, NumberRange, Regexp
from classuser import User

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret keys"

users = []

class MessageForms(FlaskForm):
    name = StringField("Имя", validators=[Length(min=2, max=30), Regexp('^[a-zA-Zа-яА-Я]+$')])
    surname = StringField("Фамилия", validators=[Length(min=1, max=30), Regexp('^[a-zA-Zа-яА-Я]+$')])
    age = IntegerField("Возраст", validators=[NumberRange(min=14, max=100)])
    password = StringField("Пароль", validators=[Length(min=8, max=12), Regexp('^[a-zA-Z0-9]+$')])
    email = EmailField("email", validators=[Email()])
    submit = SubmitField("Отправить")

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
        users.append(User(name, surname, age, password, email))
        # users.sort(key=User[0])
        return redirect(url_for('newUser'))

    return render_template('newuser.html', form=form)

@app.route('/sortnameusers')
def sortname():

    return render_template('sortnameusers.html', users=users)

@app.route('/sortsurnameusers')
def sortsurname():

    return render_template('sortsurnameusers.html', users=users)

@app.route('/sortemailusers')
def sortemail():

    return render_template('sortemailusers.html', users=users)

@app.route('/sortageusers')
def sorteage():

    return render_template('sortageusers.html', users=users)

if __name__ == '__main__':
    app.run()