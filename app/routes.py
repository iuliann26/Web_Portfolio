from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.forms import RegisterForm, LoginForm
from app.models import User
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user

main = Blueprint('main', __name__)

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        print(f"Înregistrare: {username}, {email}")

        existing_user = User.query.filter_by(email=email).first()
        print(f"Utilizator existent: {existing_user}")

        if existing_user:
            flash('Acest email este deja folosit.', 'danger')
            return redirect(url_for('main.register'))

        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password=hashed_password)

        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Înregistrare reușită!', 'success')
            return redirect(url_for('main.login'))
        except Exception as e:
            db.session.rollback()
            print(f"Eroare DB: {e}")
            flash('A apărut o eroare la crearea contului.', 'danger')
            return redirect(url_for('main.register'))

    return render_template('register.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Te-ai conectat cu succes!', 'success')
            return redirect(url_for('main.home'))  # sau pagina ta principală după login
        else:
            flash('Nume utilizator sau parolă incorecte.', 'danger')
            return redirect(url_for('main.login'))

    return render_template('login.html', form=form)


@main.route('/')
def home():
    return render_template('home.html', user=current_user)

