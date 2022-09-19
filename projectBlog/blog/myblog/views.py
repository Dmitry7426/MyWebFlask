import blog
from blog import app
from flask import render_template, request
from blog.myblog.allblog import Allbl
from blog.myblog.models import start, nblog, allblogs, duplicates, lastblogs


a = []

@app.route('/', methods=['GET', 'POST'])
def index():
    allblogs(a)
    return render_template('base.html', test=start(), blogs=a, last=lastblogs(a))

@app.route('/newblog', methods=['GET', 'POST'])
def newblog():

    if request.method == 'POST':
        author = request.form.get('author')
        nikname = request.form.get('nikname')
        briefblock = request.form.get('brieflyBlock')
        textblock = request.form.get('textPost')
        a.append(Allbl(author, nikname, briefblock, textblock))

    return render_template('newblog.html', nblog=nblog(a), res=duplicates(a))

@app.route('/allblog', methods=['POST','GET'])
def allblog():

    allblogs(a)
    # print(a)
    return render_template('allblog.html', blogs=a)

@app.route('/post/<int:value>')
def userpost(value):
    if value < 0 or value > len(a):
        return 'Такого поста не существует'
    return render_template('userpost.html', userpost=a[value - 1])