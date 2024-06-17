from flask import Flask, render_template, request
import requests
from cookbook import Cookbook

app = Flask(__name__)

cookbook = Cookbook()
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


@app.route("/", methods=['GET', 'POST'])
def home():
    global cookbook

    cookbook.clear()
    if request.method == 'GET':
        load_recipes('a')
    elif request.method == 'POST':
        load_recipes(request.form.get('letters'))

    return render_template('index.html', recipes=cookbook.recipes, letter=cookbook.letter, letters=letters)


@app.route('/<meal_id>')
def view_single_recipe(meal_id):
    chosen_recipe = cookbook.get(meal_id)
    return render_template('page.html', recipe=chosen_recipe)


def load_recipes(letter):
    global cookbook

    url = f"https://www.themealdb.com/api/json/v1/1/search.php?f={letter}"
    data = requests.get(url)
    data.raise_for_status()

    json = data.json()

    cookbook.letter = letter

    if json['meals']:
        for meal in json['meals']:
            cookbook.add_recipe(meal)


if __name__ == "__main__":
    app.run(debug=True)
