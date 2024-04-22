from flask import *
from flask import Flask
import os


app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run()
