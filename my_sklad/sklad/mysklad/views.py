import sklad
from sklad import app
from flask import render_template, request, flash, redirect, url_for, session, Blueprint, Markup
from sklad.mysklad.creat_base import Tests
from sklad.mysklad.models import User, RegistrationForm, LoginUser, AutorizeAdmin

admlogin = ['root', 'admin']


@app.route('/', methods=['GET', 'POST'])
def index():
    # names = readname.AdminTable.query.filter_by(name='Дмитрий')
    names = sklad.AdminTable.query.filter_by(name='Дмитрий').first()
    names2 = Tests.my(15)
    return render_template('base.html', names=names, names2=names2)

@app.route('/register', methods=['GET','POST'])
def register_adm():
    form = RegistrationForm(request.form)

    if request.method == 'POST':
        username = request.form.get('username')
        w = sklad.AdminTable('family', username, 'middlname', 'pozition', 'pwd')
        sklad.db.session.add(w)
        sklad.db.session.commit()



    return render_template('base.html', form=form)


@app.route('/autorizeadmin', methods=['GET','POST'])
def autorize():
    form = AutorizeAdmin(request.form)

    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')

        if username in admlogin and password in admlogin:
            wait_time = 3000
            seconds = wait_time / 1000
            redirect_url = '/index'

            session['username'] = request.form['username']
            message = Markup("<h1>Отлично! Вы авторизовались!</h1>")
            flash(message)
            if 'username' in session:
                user = session['username']
                print(user)
            return f"<html><body><p>You will be redirected in { seconds } seconds</p>" \
                   f"<script>var timer = setTimeout(function() {{window.location='{ redirect_url }'}}, { wait_time });</script></body></html>"

        else:
            message = Markup("<h1>Не верный логин или пароль! Попробуйте еще раз!</h1>")
            flash(message)


    return render_template('login.html', form=form)

@app.route('/index', methods=['GET', 'POST'])
def redir():
    return render_template('index.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('/autorizeadmin'))