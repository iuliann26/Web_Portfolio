from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.forms import RegisterForm, LoginForm
from app.models import User
from flask_login import login_user, logout_user, current_user, login_required
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user
from app.forms import LoginForm

main = Blueprint('main', __name__)

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        # Verifică dacă emailul există deja
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Acest email este deja folosit.', 'danger')
            return redirect(url_for('main.register'))

        # Creează utilizatorul și setează parola criptată
        new_user = User(username=username, email=email)
        new_user.set_password(password)

        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Înregistrare reușită! Te poți autentifica.', 'success')
            return redirect(url_for('main.login'))
        except Exception as e:
            db.session.rollback()
            print(f"Eroare DB: {e}")
            flash('A apărut o eroare la crearea contului.', 'danger')
            return redirect(url_for('main.register'))

    return render_template('register.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            return redirect(url_for('main.home'))
        else:
            flash('Username sau parolă incorecte.', 'danger')
    return render_template('login.html', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@main.route('/')
def home():
    return render_template('home.html', user=current_user)

