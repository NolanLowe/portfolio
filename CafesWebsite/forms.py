from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.datetime import TimeField
from wtforms.fields.simple import PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('name', validators=[DataRequired()])
    password = PasswordField('name', validators=[DataRequired()])
    submit = SubmitField('login')


class RegisterForm(FlaskForm):
    username = StringField('name', validators=[DataRequired()])
    password = PasswordField('name', validators=[DataRequired()])
    submit = SubmitField('Create Account')


class CafeForm(FlaskForm):
    name = StringField('Cafe Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    map_link = StringField('Map Link')
    open = TimeField("Opening Time")
    close = TimeField("Closing Time")
    add_cafe = SubmitField('Add Cafe')
