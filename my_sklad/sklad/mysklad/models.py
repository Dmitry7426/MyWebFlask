from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, EqualTo
from werkzeug.security import generate_password_hash, check_password_hash


class User:
    def __init__(self, family, name, midlname, pozition, mail, password):
        self.family = family
        self.name = name
        self.midlname = midlname
        self.pozition = pozition
        self.mail = mail
        self.pwdhash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)




class RegistrationForm(FlaskForm):
    username = StringField('Имя пользователя', [InputRequired()])
    password = PasswordField('Пароль', [InputRequired(), EqualTo('confirm', message='Пароли должны совпадать')])
    confirm = PasswordField('Повторите пароль', [InputRequired()])


class LoginUser(FlaskForm):
    username = StringField('Имя пользователя', [InputRequired()])
    password = PasswordField('Пароль', [InputRequired()])


class AutorizeAdmin(FlaskForm):
    username = StringField('Имя пользователя', [InputRequired()])
    password = PasswordField('Пароль', [InputRequired()])
