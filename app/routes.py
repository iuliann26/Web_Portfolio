from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.forms import RegisterForm, LoginForm
from app.models import User
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user
from app.forms import LoginForm
from flask_login import login_required, current_user
from flask_login import login_user, logout_user

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html', user=current_user)



@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    print("A intrat în ruta /register")

    if form.validate_on_submit():
        print("Formular validat")
        print("Email:", form.email.data)
        print("Parolă:", form.password.data)

        # Hash parolă
        hashed_pw = generate_password_hash(form.password.data, method='pbkdf2:sha256')
        print("Parola hashed:", hashed_pw)

        # Creează utilizatorul
        user = User(email=form.email.data, password=hashed_pw)
        print("User creat:", user)

        # Adaugă utilizatorul în DB
        db.session.add(user)
        try:
            db.session.commit()
            print("Contul a fost salvat în DB")
            flash('Cont creat cu succes!', 'success')
        except Exception as e:
            print("Eroare la salvarea în DB:", e)

        return redirect(url_for('main.login'))
    
    else:
        print("Formularul NU a trecut de validare")
        print("Erori de validare:", form.errors)

    return render_template('register.html', form=form)


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Autentificare reușită!', 'success')
            return redirect(url_for('main.home'))  # sau altă pagină
        else:
            flash('Email sau parolă incorecte', 'danger')
    return render_template('login.html', form=form)
def logout():
    logout_user()
    return redirect(url_for('main.home'))
