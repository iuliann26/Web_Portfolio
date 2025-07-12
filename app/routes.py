from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.forms import RegisterForm, LoginForm
from app.models import User
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user
from app.forms import LoginForm
from flask_login import login_required, current_user
from flask_login import login_user, logout_user
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html', user=current_user)



@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
#verifica dac este mail existent
        existing_user_email = User.query.filter_by(email=form.email.data).first()
        if existing_user_email:
            flash("Există deja un cont cu acest email.", "warning")
            return redirect(url_for('main.register'))


    return render_template('register.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Autentificare reușită!', 'success')
            return redirect(url_for('main.dashboard'))  # sau altă pagină
        else:
            flash('Email sau parolă incorecte', 'danger')
    return render_template('login.html', form=form)
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@main.app_context_processor

def inject_now():
    return {'now': lambda: datetime.now()}