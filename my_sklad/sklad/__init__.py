
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sklad.db'
app.config['SECRET_KEY'] = 'MySecretKey'
db.init_app(app)


class AdminTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    family = db.Column(db.String(50))
    name = db.Column(db.String(50))
    middlname = db.Column(db.String(50))
    pozition = db.Column(db.String(50))
    mail = db.Column(db.String(50))
    pwd = db.Column(db.String(255))

    def __init__(self, family, name, middlname, pozition, mail,pwd):
        self.family = family
        self.name = name
        self.middlname = middlname
        self.pozition = pozition
        self.mail = mail
        self.pwd = pwd

# class Vendor(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     vendor = db.Columb(db.String(50))
#
#     def __init__(self, vendor):
#         self.vendor = vendor


with app.app_context():
    db.create_all()

import sklad.mysklad.views