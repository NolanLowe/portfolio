import os

import flask_login
from flask import *
from flask import Flask
from flask_login import login_required, login_user, logout_user, LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.exc import PendingRollbackError, IntegrityError
from sqlalchemy.orm import DeclarativeBase, backref
from werkzeug.security import generate_password_hash, check_password_hash

from forms import *


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(Integer, primary_key=True, nullable=False)
    username = db.Column(String(25), unique=True, nullable=False)
    password = db.Column(String(200), nullable=False)

    tasks = db.relationship("ToDo", backref=backref("creator", uselist=False))



class ToDo(db.Model):
    __tablename__ = "todos"
    id = db.Column(Integer, primary_key=True, nullable=False)
    userid = db.Column(Integer, ForeignKey("users.id"), nullable=False)
    description = db.Column(String(25), nullable=False)
    by_day = db.Column(db.Date, nullable=True)
    by_hour = db.Column(db.Time, nullable=True)
    __table_args__ = (db.UniqueConstraint('description', 'userid'),)


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

login_manager = LoginManager()
login_manager.init_app(app)

db.init_app(app)

with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    user = db.session.execute(db.select(User).where(User.id == user_id)).scalar_one()
    if user is None:
        return None
    else:
        return user


@app.route("/")
def home():
    if flask_login.current_user.is_authenticated:
        return redirect(url_for('tasks'))
    else:
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.execute(db.select(User).where(User.username == form.username.data)).scalar_one()
        if check_password_hash(user.password, form.password.data):
            login_user(user)

            flash('Logged in successfully.')

            return redirect(url_for('tasks'))
        else:
            flash('Incorrect password or username.')
    return render_template('login.html', form=form)


@login_required
@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    form = TaskForm()

    if request.method == "POST" and 'finishtasks' in request.form:
        print(request.json)

    elif form.validate_on_submit():
        task = ToDo(
            description=form.description.data,
            by_day=form.day.data,
            by_hour=form.hour.data,
            creator=flask_login.current_user
        )
        for existing_task in flask_login.current_user.tasks:
            if task.description == existing_task.description and task.userid == existing_task.userid:
                flash("task already exists!")
                new_form = TaskForm()
                return render_template('tasks.html', form=new_form)

        db.session.add(task)
        db.session.commit()
        new_form = TaskForm()
        return render_template('tasks.html', form=new_form)

    return render_template('tasks.html', form=form)



@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        try:
            user = User(
                username=form.username.data,
                password=generate_password_hash(form.password.data, method='scrypt', salt_length=16),
            )
            db.session.add(user)
            db.session.commit()

            login_user(user)

            flash('Created new account successfully.')
            flash('Logged in automatically.')
            return redirect(url_for('tasks', user_id=user.id))

        except:
            flash("acct already exists / problem with uname / pass")

    return render_template('register.html', form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)
