from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.datetime import DateField, DateTimeField, TimeField
from wtforms.fields.simple import PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, optional


class LoginForm(FlaskForm):
    username = StringField('name', validators=[DataRequired()])
    password = PasswordField('name', validators=[DataRequired()])
    submit = SubmitField('login')


class RegisterForm(FlaskForm):
    username = StringField('name', validators=[DataRequired()])
    password = PasswordField('name', validators=[DataRequired()])
    submit = SubmitField('Create Account')


class TaskForm(FlaskForm):
    description = StringField('name', validators=[DataRequired()])
    day = DateField('day', validators=[optional()])
    hour = TimeField('hour', validators=[optional()])


class CompleteTaskForm(FlaskForm):
    submit = SubmitField('Mark Complete')

