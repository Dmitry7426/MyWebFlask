from flask import Flask, render_template
from math import sqrt
import classParce
import classInOutFile

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
    d = b ** 2 - 4 * a * c

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
    return render_template('parce.html')


@app.route('/parceInFile')
def parceinfile():
    return render_template('parceInFile.html')


@app.route('/parce/small')
def parcesmall():
    st = classParce.parceListArea('small')
    slovar = (st.pathUrlToClassArea())
    return render_template('parceSmall.html', slovar=slovar)


@app.route('/parce/medium')
def parcemedium():
    st = classParce.parceListArea('medium')
    slovar = (st.pathUrlToClassArea())
    return render_template('parceSmall.html', slovar=slovar)


@app.route('/parce/big')
def parcebig():
    st = classParce.parceListArea('big')
    slovar = (st.pathUrlToClassArea())
    return render_template('parceSmall.html', slovar=slovar)


@app.route('/parce/large')
def parcelarge():
    st = classParce.parceListArea('large')
    slovar = (st.pathUrlToClassArea())
    return render_template('parceSmall.html', slovar=slovar)


@app.route('/parce/largest')
def parcelargest():
    st = classParce.parceListArea('largest')
    slovar = (st.pathUrlToClassArea())
    return render_template('parceSmall.html', slovar=slovar)


@app.route('/parce/millioners')
def parcemillioners():
    st = classParce.parceListArea('millioners')
    slovar = (st.pathUrlToClassArea())
    return render_template('parceSmall.html', slovar=slovar)


@app.route('/parce/parceinfilesmall')
def parceinfilesmall():
    st = classInOutFile.parceListInOut('small')
    st.writeFile()
    slovar = st.readFile()
    return render_template('parceSmallInFile.html', slovar=slovar)


@app.route('/parce/parceinfilemedium')
def parceinfilemedium():
    st = classInOutFile.parceListInOut('medium')
    st.writeFile()
    slovar = st.readFile()
    return render_template('parceSmallInFile.html', slovar=slovar)


@app.route('/parce/parceinfilebig')
def parceinfilebig():
    st = classInOutFile.parceListInOut('big')
    st.writeFile()
    slovar = st.readFile()
    return render_template('parceSmallInFile.html', slovar=slovar)


@app.route('/parce/parceinfilelarge')
def parceinfilelarge():
    st = classInOutFile.parceListInOut('large')
    st.writeFile()
    slovar = st.readFile()
    return render_template('parceSmallInFile.html', slovar=slovar)


@app.route('/parce/parceinfilelargest')
def parceinfilelargest():
    st = classInOutFile.parceListInOut('largest')
    st.writeFile()
    slovar = st.readFile()
    return render_template('parceSmallInFile.html', slovar=slovar)


@app.route('/parce/parceinfilemillioners')
def parceinfilemillioners():
    st = classInOutFile.parceListInOut('millioners')
    st.writeFile()
    slovar = st.readFile()
    return render_template('parceSmallInFile.html', slovar=slovar)


if __name__ == '__main__':
    app.run()
