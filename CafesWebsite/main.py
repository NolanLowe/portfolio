import os

from flask import *
from flask import Flask
from flask_login import login_user, logout_user, LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Column, Time
from sqlalchemy.orm import DeclarativeBase, class_mapper, ColumnProperty
from werkzeug.security import generate_password_hash, check_password_hash

from forms import *


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class User(db.Model, UserMixin):
    __tablename__ = "admin"
    id = db.Column(Integer, primary_key=True, nullable=False)
    username = db.Column(String(25), unique=True, nullable=False)
    password = db.Column(String(200), nullable=False)


class Cafe(db.Model):
    __tablename__ = "cafes"
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(50), nullable=False)
    description = Column(String(100), nullable=True)
    address = Column(String(150), nullable=True)
    open = Column(Time, nullable=True)
    close = Column(Time, nullable=True)


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


def get_cafes():
    return db.session.execute(db.select(Cafe)).scalars().all()


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.execute(db.select(User).where(User.username == form.username.data)).scalar_one()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)

                flash('Logged in successfully.')

                return redirect(url_for('home'))
            else:
                # wrong password
                flash("Incorrect password / username")
        else:
            # no matching username
            flash("Incorrect password / username")
    return render_template('login.html', form=form)


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
            return redirect(url_for('home'))

        except:
            flash("acct already exists / problem with uname / pass")

    return render_template('register.html', form=form)


@app.route("/")
def home():
    cafes = get_cafes()
    form = CafeForm()
    return render_template('index.html', form=form, cafes=cafes)


@app.route('/add_cafe', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = Cafe(
            name=form.name.data,
            description=form.description.data,
            address=form.map_link.data,
            open=form.open.data,
            close=form.close.data
        )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('addCafe.html', form=form)


@app.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run()
