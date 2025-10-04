"""Formulare pentru utilizatori (înregistrare, login)."""
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length, ValidationError

from app.models import User


class RegisterForm(FlaskForm):
    """Formular de înregistrare utilizator."""

    csrf_token = StringField("CSRF Token", validators=[DataRequired()])
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=3, max=25)]
    )
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Parolă", validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("Înregistrează-te")

    def validate_email(self, email):
        """Validate that email is unique."""
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Acest email este deja folosit.")

    def validate_username(self, username):
        """Validate that username is unique."""
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Numele de utilizator este deja folosit.")


class LoginForm(FlaskForm):
    """Formular pentru login utilizator."""

    username = StringField(
        "Username", validators=[DataRequired(), Length(min=4, max=25)]
    )
    password = PasswordField("Parola", validators=[DataRequired()])
    submit = SubmitField("Autentificare")
