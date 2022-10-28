import sklad
from sklad import app
from flask import render_template, request, flash, redirect, session, Markup
from sklad.mysklad.models import User, RegistrationForm, LoginUser, AutorizeAdmin
from werkzeug.security import check_password_hash


admlogin = ['root', 'admin']


# Стартовая страница Index
@app.route('/', methods=['GET', 'POST'])
def index():
    if 'username' in session:
        user = session['username']
        message = Markup(f'<h1>Пользователь {user} авторизован в системе!</h1>')
        flash(message)
    if 'username' not in session:
        message = Markup(f'<h1></h1>')
        flash(message)

    return render_template('index.html')


# Регистрация пользователя в БД
@app.route('/register', methods=['GET', 'POST'])
def register_adm():
    form = RegistrationForm(request.form)

    if request.method == 'GET':
        message = Markup("<h1></h1>")
        flash(message)

    if request.method == 'POST':
        pas1 = request.form.get('password')
        pas2 = request.form.get('confirm_password')
        print(pas1, pas2)
        if str(pas1) == str(pas2):

            message = Markup("<h1>Отлично! Вы зарегистрировались!</h1>")
            flash(message)
            user = User(request.form.get('family'), request.form.get('name'),
                        request.form.get('midlname'), request.form.get('pozition'), request.form.get('mail'),
                        request.form.get('password'))
            w = sklad.AdminTable(user.family, user.name, user.midlname, user.pozition, user.mail, user.pwdhash)
            sklad.db.session.add(w)
            sklad.db.session.commit()
        else:
            message = Markup("<h1>Пароли не совпадают! Попробуйте еще раз!</h1>")
            flash(message)

    return render_template('register.html', form=form)


# Авторизация супер-пользователя
@app.route('/autorizeadmin', methods=['GET', 'POST'])
def autorize():
    form = AutorizeAdmin(request.form)

    if request.method == 'GET':
        message = ''
        flash(message)

    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')

        if username in admlogin and password in admlogin:
            # wait_time = 3000
            # seconds = wait_time / 1000
            # redirect_url = '/index'

            session['username'] = request.form['username']
            message = Markup("<h1>Отлично! Вы авторизовались!</h1>")
            flash(message)
            if 'username' in session:
                user = session['username']
                print(user)
            # return f"<html><body><p>You will be redirected in { seconds } seconds</p>" \
            # f"<script>var timer = setTimeout(function() {{window.location='{ redirect_url }'}},
            # { wait_time });</script></body></html>"

        else:
            message = Markup("<h1>Не верный логин или пароль! Попробуйте еще раз!</h1>")
            flash(message)
            message_aut = Markup('<a href="register">Я хочу зарегистрироваться!</a>')
            flash(message_aut)

    return render_template('login.html', form=form)


# Вход в систему под обычным пользователем
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginUser()

    if 'username' in session:
        user = session['username']
        message = Markup(f'<h1>Пользователь {user} уже авторизован!</h1>')
        flash(message)
        return redirect('/')

    if request.method == 'POST':

        usr = sklad.AdminTable.query.filter_by(mail=request.form.get('username')).first()
        if usr:
            pas = check_password_hash(usr.pwd, request.form.get('password'))
            if pas:
                session['username'] = request.form['username']
                message = Markup("<h1>Отлично! Вы авторизовались!</h1>")
                flash(message)
                return redirect('/')
            else:
                message = Markup("<h1>Не верный пароль!!</h1>")
                flash(message)
        else:
            message = Markup("<h1>Такого пользователя нет в базе! Попробуйте еще раз!</h1>")
            flash(message)
            return redirect('login')

    return render_template('loginuser.html', form=form)


# Взврат на начальную страницу
@app.route('/index', methods=['GET', 'POST'])
def redir():
    return render_template('index.html')


# Очистка сессий и возврат на начальную страницу проекта
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('index')

<<<<<<< HEAD
# просто добавил строчку
=======

# ветка JOBS
>>>>>>> jobs
