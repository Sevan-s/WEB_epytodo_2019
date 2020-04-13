from flask_wtf import FlaskForm
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

class LoginForm(FlaskForm):
    username = TextField('username', validators=[validators.required()])
    password = TextField('password', validators=[validators.required()])


class RegisterForm(FlaskForm):
    login = TextField('username', validators=[validators.required()])
    key = TextField('password', validators=[validators.required()])
