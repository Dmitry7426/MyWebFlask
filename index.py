from flask import Flask, render_template
from math import sqrt
import requests
import re
import json
import csv
from bs4 import BeautifulSoup
import classParce

app = Flask(__name__)

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

# Лекции
@app.route('/colors')
def colors():
    listofcolors = ['green', 'red', 'yellow', 'blue']
    return render_template('colors.html', lst=listofcolors)

@app.route('/solve/<int:a>/<int:b>/<int:c>')
def solve(a, b, c):
    d = b**2 - 4 * a * c

    # if d > 0:
    #     x1 = (-b + (math.sqrt(d)) / (2 * a))
    #     x2 = (-b - (math.sqrt(d)) / (2 * a))
    # elif d == 0:
    #     x1 = -b / 2 * a
    # else:
    #     x1 = ''

    return render_template('solve.html', dis=d, a=a, b=b, c=c, sqrt=sqrt)


@app.route('/tables')
def tables():
    slovar = {'Челябинск': 1148000, 'Москва': 12954233}
    return render_template('tables.html', slovar=slovar)



@app.route('/parce')
def parce():
    # st = classParce.parceListArea('small')
    # st.printUrl()
    # slovar = (st.pathUrlToClassArea())
    return render_template('parce.html')

@app.route('/parce/small')
def parceSmall():
    st = classParce.parceListArea('small')
    # st.printUrl()
    slovar = (st.pathUrlToClassArea())
    return render_template('parceSmall.html', slovar=slovar)

@app.route('/parce/medium')
def parceMedium():
    st = classParce.parceListArea('medium')
    # st.printUrl()
    slovar = (st.pathUrlToClassArea())
    return render_template('parceMedium.html', slovar=slovar)

@app.route('/parce/big')
def parceBig():
    st = classParce.parceListArea('big')
    # st.printUrl()
    slovar = (st.pathUrlToClassArea())
    return render_template('parceBig.html', slovar=slovar)

@app.route('/parce/large')
def parceLarge():
    st = classParce.parceListArea('large')
    # st.printUrl()
    slovar = (st.pathUrlToClassArea())
    return render_template('parceLarge.html', slovar=slovar)

@app.route('/parce/largest')
def parceLargest():
    st = classParce.parceListArea('largest')
    # st.printUrl()
    slovar = (st.pathUrlToClassArea())
    return render_template('parceLargest.html', slovar=slovar)

@app.route('/parce/millioners')
def parceMillioners():
    st = classParce.parceListArea('millioners')
    # st.printUrl()
    slovar = (st.pathUrlToClassArea())
    return render_template('parceMillioners.html', slovar=slovar)


if __name__ == '__main__':
    app.run()
