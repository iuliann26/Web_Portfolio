from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.forms import RegisterForm
from app.models import User
from app import db
from werkzeug.security import generate_password_hash

main = Blueprint('main', __name__)

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash("Există deja un cont cu acest email.", "warning")
            return redirect(url_for('main.register'))

        hashed_pw = generate_password_hash(form.password.data)
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_pw
        )

        db.session.add(new_user)
        db.session.commit()
        flash("Cont creat! Acum te poți loga.", "success")
        return redirect(url_for('main.login'))

    return render_template('register.html', form=form)


@main.route('/login', methods=['GET', 'POST'])
def login():
    return "Login page (în construcție)"
