from flask import Blueprint, render_template, redirect, url_for
from db_data import db_session
from db_data.users import User
from forms.user import RegisterForm, LoginForm


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        query = db_sess.query(User).filter(User.login == form.name.data)
        for user in query:
            if user.check_password(form.password.data):
                return redirect("????") # fix
    return render_template('login_.html')


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('signup_.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).count() or \
                db_sess.query(User).filter(User.login == form.name.data).count():
            return render_template('signup_.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            login=form.name.data,
            email=form.email.data,
            is_admin=False
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('signup_.html', title='Регистрация', form=form)
