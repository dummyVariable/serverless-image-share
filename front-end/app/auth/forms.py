from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    login = SubmitField('Login')

class SignUpForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Password', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    login = SubmitField('Register')

class ConfirmSignUpForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired()])
    code = IntegerField('Code', validators=[DataRequired()])
    login = SubmitField('Register')