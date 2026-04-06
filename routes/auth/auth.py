from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import User, db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, current_user, login_user, logout_user
from datetime import timedelta

auth_routes = Blueprint('auth', __name__, url_prefix='/auth')


@auth_routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email'].strip()
        password = request.form['password'].strip()
        remember = request.form.get('remember') == 'on'

        if not email or not password:
            flash("Заполните поля", 'danger')
            return redirect(url_for('auth.login'))

        user = User.query.filter_by(email=email).first()

        if not user:
            flash("Пользователь не найден", 'danger')
            return redirect(url_for('auth.login'))

        if not check_password_hash(user.password, password):
            flash("Пароль неверный", 'danger')
            return redirect(url_for('auth.login'))

        login_user(user, remember=remember, duration=timedelta(days=30))
        flash('Вы успешно вошли', 'success')
        return redirect(url_for('main.home'))

    return render_template("auth/login.html")


@auth_routes.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username'].strip()
        email = request.form['email'].strip()
        password = request.form['password'].strip()
        password2 = request.form['password2'].strip()

        if not username or not email or not password or not password2:
            flash("Заполните поля", 'danger')
            return redirect(url_for('auth.register'))

        if password != password2:
            flash("Пароли не совпадают", 'danger')
            return redirect(url_for('auth.register'))

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Такой пользователь уже существует", "danger")
            return redirect(url_for('auth.register'))

        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            flash("Такой email уже используется", "danger")
            return redirect(url_for('auth.register'))

        try:
            hashed_password = generate_password_hash(password)

            user = User(
                username=username,
                hashed_password=hashed_password,
                email=email
            )

            db.session.add(user)
            db.session.commit()

            login_user(user, remember=True, duration=timedelta(days=30))
            flash('Аккаунт успешно создан', 'success')
            return redirect(url_for('main.home'))

        except Exception as e:
            db.session.rollback()
            flash('Ошибка при создании пользователя', 'danger')
            return render_template('auth/register.html')

    return render_template("auth/register.html")


@auth_routes.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Вы вышли из аккаунта', 'success')
    return redirect(url_for('main.home'))