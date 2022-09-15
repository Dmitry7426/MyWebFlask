from flask import Flask, render_template
app = Flask(__name__)
import sudoku_app.sudoku.views
