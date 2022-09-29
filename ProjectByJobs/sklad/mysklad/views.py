import sklad
from sklad import app
from flask import render_template, request

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        w = 'гет запрос'

    if request.method == 'POST':
        w = 'пост запрос'

    return render_template('base.html', w=w)