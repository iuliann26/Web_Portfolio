from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from app.models import User

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Parolă', validators=[DataRequired(), Length(min=6)])
    confirm = PasswordField('Confirmă parola', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Înregistrează-te')



    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Acest email este deja folosit.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Parola', validators=[DataRequired()])
    submit = SubmitField('Autentificare')