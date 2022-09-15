from sudoku_app import app
from flask import render_template, request

from sudoku_app.sudoku.models import arr, testGorizonty


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        for i in range(9):
            for j in range(9):

                arr[i][j] = request.form.get(str(i) + str(j))
        # print(arr)
        testGorizonty(arr)

    return render_template('base.html', arr=arr)