from sudoku_app import app
from flask import render_template, request

from sudoku_app.sudoku.models import arr, sudokuapp


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'post':
        for i in range(9):
            for j in range(9):
                arr[i][j] = int(request.form.get(str(i) + str(j)))
    sudokuapp(arr)
    return render_template('base.html', arr=arr)