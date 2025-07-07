from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Parolă', validators=[DataRequired(), Length(min=6)])
    confirm = PasswordField('Confirmă parola', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Înregistrează-te')
